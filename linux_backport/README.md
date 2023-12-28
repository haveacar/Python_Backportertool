
# Backporter

Backporter is a Python-based tool that streamlines the process of applying patches to files. It efficiently reads files, detects differences between two file versions, and applies these differences as a patch to a target file. This tool is especially useful for managing file version control and updating processes.

## Features

- **Efficient File Handling**: Reads files line-by-line, enabling it to handle large files effectively.
- **Patch Generation**: Creates a patch by identifying the differences between two versions of a file.
- **Patch Application**: Applies patches to target files, complete with detailed operation logs.
- **Detailed Output**: Provides an output of the patch application and a comprehensive log file with change details.

## Installation

To install Backporter, clone the repository or download the source code:

```bash
git clone https://github.com/haveacar/Backporter.git
cd Backporter
```

## Usage

Run Backporter by executing the main function with three arguments: the original file, the modified file, and the target file for the patch:

```bash
python backporter.py <original_file> <modified_file> <target_file>
```

After running the command, Backporter will generate two files:

- `result.c`: The target file with the patch applied.
- `log.txt`: A log file detailing the changes made.

## Contact

- **Developer**: Your Name
- **Email**: haveacar.zhovnirl@gmail.com
- **Project Link**: [https://github.com/haveacar/Backporter](https://github.com/haveacar/Backporter)
