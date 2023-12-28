import difflib
import os

def find_file_in_root_then_dirs(filename:str):
    """
    Search for a file in the root directory first, then in its subdirectories.
    :param filename: The name of the file to search for.

    :return: The path of the file if found, otherwise None.
    """
    try:
        root_directory = os.path.dirname(__file__)
    except NameError:
        root_directory = os.getcwd()  # Current working directory as a fallback

    # First, check in the root directory
    if filename in os.listdir(root_directory):
        return os.path.join(root_directory, filename)

    # If not found, search in subdirectories
    for root, dirs, files in os.walk(root_directory):
        if filename in files:
            return os.path.join(root, filename)

    return None

class Backporter:
    def __init__(self, before_file:str, after_file:str, target_file:str):
        self.before = self._read_file(before_file)
        self.after = self._read_file(after_file)
        self.target = self._read_file(target_file)

    @staticmethod
    def _find_file_in_root_then_dirs(filename: str):
        """
        Search for a file in the root directory first, then in its subdirectories.
        :param filename: The name of the file to search for.
        :return: The path of the file if found, otherwise None.
        """
        root_directory = os.path.dirname.__file__

        # First, check in the root directory
        if filename in os.listdir(root_directory):
            return os.path.join(root_directory, filename)

        # If not found, search in subdirectories
        for root, dirs, files in os.walk(root_directory):
            if filename in files:
                return os.path.join(root, filename)

        return None

    @staticmethod
    def _read_file(filename:str):
        file_patch = find_file_in_root_then_dirs(filename)
        with open(file_patch, 'r') as file:
            return file.readlines()

    @staticmethod
    def write_file(filename, data):
        with open(filename, 'w') as file:
            file.writelines(data)

    def create_patch(self):
        return difflib.unified_diff(self.before, self.after, lineterm='')


    def apply_patch(self):
        patch = self.create_patch()
        patch_obj = difflib.PatchSet(patch)
        result = list(self.target)
        log = []

        for i, hunk in enumerate(patch_obj[0]):
            try:
                # Apply hunk
                result = hunk.apply(result)
                log.append(f"Hunk {i + 1} applied successfully.\n")
            except Exception as e:
                # Handle merge conflict
                log.append(f"Merge conflict in Hunk {i + 1}: {e}\n")
                log.append(f"Conflict at lines {hunk.start} to {hunk.end}\n")

        return result, log

