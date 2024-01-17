import difflib
import os
import sys
from datetime import datetime
from typing import List, Tuple, Optional

def find_file_in_root_then_dirs(filename: str) -> Optional[str]:
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
    def __init__(self, before_file: str, after_file: str, target_file: str) -> None:
        """
        Initialize the Backporter object.

        :param before_file: The file path before changes.
        :param after_file: The file path after changes.
        :param target_file: The file path where changes need to be applied.
        """
        self._logs = []
        self.event('INFO started successfully.')
        try:
            self.before = list(self._read_file(before_file))
            self.after = list(self._read_file(after_file))
            self.target = list(self._read_file(target_file))
        except FileNotFoundError as e:
            self.write_file('log.txt', self._logs)
            print(e)
            sys.exit(1)

    def _read_file(self, filename: str) -> List[str]:
        """Read a file and return its lines."""
        file_path = find_file_in_root_then_dirs(filename)
        if file_path is None:
            text = f"ERROR File '{filename}' not found in project directory or subdirectories."
            self.event(text)
            raise FileNotFoundError(text)

        with open(file_path, 'r') as file:
            return file.readlines()

    def write_file(self, filename: str, data: List[str]) -> None:
        """
        Write data to a file.

        :param filename: The name of the file to write to.
        :param data: The data to write to the file.
        """
        with open(filename, 'w') as file:
            file.writelines(data)

    def event(self, event: str) -> None:
        timestamp = datetime.now()
        event_string = f'{timestamp} {event}\n'
        self._logs.append(event_string)

    def create_patch(self) -> List[str]:
        return list(difflib.unified_diff(self.before, self.after, lineterm=''))

    def apply_patch(self) -> Tuple[List[str], List[str]]:
        patch_lines = self.create_patch()
        result = list(self.target)

        i = 0
        for line in patch_lines:
            if line.startswith('@@'):
                start_line = int(line.split()[1].split(',')[0][1:])
                i = start_line - 1
            elif line.startswith('-'):
                if i < len(result):
                    removed_line = result.pop(i)
                    self.event(f"INFO Line {i + 1} {removed_line.strip()} removed.")
            elif line.startswith('+'):
                result.insert(i, line[1:])
                self.event(f"INFO Line {i + 1} {line[1:].strip()} added.")
                i += 1
            elif line.startswith(' '):
                i += 1

        return result, self._logs