import difflib


class Backporter:

    def __init__(self, before_file, after_file, target_file):

        self.before = self.read_file(before_file)
        self.after = self.read_file(after_file)
        self.target = self.read_file(target_file)

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as file:
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

