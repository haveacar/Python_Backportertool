import sys
from controls import Backporter

# files names
RESULT_FILE_NAME = 'result.c'
LOG_FILE_NAME = 'log.txt'


def main(before_file, after_file, target_file):
    backporter = Backporter(before_file, after_file, target_file)
    result, log = backporter.apply_patch()
    Backporter.write_file(RESULT_FILE_NAME, result)
    Backporter.write_file(LOG_FILE_NAME, log)
    print("Backporting completed. Check 'result.c' and 'log.txt' for details.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python backporter.py <before_file> <after_file> <target_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
