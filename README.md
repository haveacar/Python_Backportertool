
# Backporter

Backporter is a Python-based tool designed for Linux systems that streamlines the process of applying patches to files. It efficiently reads files, detects differences between two file versions, and applies these differences as a patch to a target file. Optimized for Linux file systems and commands, this tool is particularly useful for managing file version control and updating processes in Linux environments.

## Features

- **Efficient File Handling**: Reads files line-by-line, enabling it to handle large files effectively.
- **Patch Generation**: Creates a patch by identifying the differences between two versions of a file.
- **Patch Application**: Applies patches to target files, complete with detailed operation logs.
- **Detailed Output**: Provides an output of the patch application and a comprehensive log file with change details.

## Installation

To install Backporter, clone the repository or download the source code:

```bash
git clone git@github.com:haveacar/Python_Backportertool.git
```

## Usage

Run Backporter by executing the main function with three arguments: the original file, the modified file, and the target file for the patch:

```bash
python backporter.py <original_file> <modified_file> <target_file>
```
Example:
```bash
python backporter.py kernel-4.18.0-477.27.1.el8_856gbnlwn kernel-4.18.0-513.5.1.el8_92fqrcwu_ l2cap_core.cf7zq5cwb
```

After running the command, Backporter will generate two files:

- `result.c`: The target file with the patch applied.
- `log.txt`: A log file detailing the changes made.

## Testing

To ensure the reliability of the Backporter tool, a suite of unit tests is included. These tests cover all major functionalities, including file handling, patch generation, and application.

To run the tests, navigate to the project directory and execute:
```bash
python -m unittest
```
This command will automatically discover and run all tests in the tests folder. Ensure all tests pass to verify the tool is functioning correctly, especially after making any changes to the code.

## Continuous Integration

This project uses GitHub Actions for continuous integration. Every push to the `main` branch and every pull request to `main` triggers automated linting with flake8 and unit testing using Python's built-in unittest framework. This ensures code quality and functional integrity throughout the development process.


## Contact


- **Developer**: Daniel Govnir
- **Email**: haveacar.zhovnirl@gmail.com
- **Project Link**: [https://github.com/haveacar/Backporter](https://github.com/haveacar/Backporter)
