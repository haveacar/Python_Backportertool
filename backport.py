import sys
from controls import Backporter

# files names
RESULT_FILE_NAME = 'result.c'
LOG_FILE_NAME = 'log.txt'


def main(before_file:str, after_file:str, target_file:str):
    backporter = Backporter(before_file, after_file, target_file)
    result, log = backporter.apply_patch()
    backporter.write_file(RESULT_FILE_NAME, result)
    backporter.event(f'INFO Backporting completed. Check {RESULT_FILE_NAME}')
    backporter.write_file(LOG_FILE_NAME, log)
    print(f"Backporting completed. Check '{RESULT_FILE_NAME}' and '{LOG_FILE_NAME}' for details.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python backporter.py <before_file> <after_file> <target_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
