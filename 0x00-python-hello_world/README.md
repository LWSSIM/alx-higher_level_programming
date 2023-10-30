# 0x00-python-hello_world

**0x00-python-hello_world** is a project that focuses on Python programming and shell scripting. It aims to provide solutions to basic tasks in Python and shell scripting, adhering to specific coding and style requirements. The project's codebase covers various aspects of Python scripting and demonstrates the use of Python 3.8.5, as well as shell scripting on Ubuntu 20.04 LTS.

## Requirements

### Python Scripts

- **Editor Choices**: You are allowed to use the text editors vi, vim, or emacs for editing the Python scripts.
- **Python Version**: All Python scripts should be written in Python 3.8.5.
- **File Ending**: All Python files should end with a new line.
- **Shebang**: The first line of all your files should be exactly `#!/usr/bin/python3`.
- **README.md**: A `README.md` file at the root of the repository is mandatory.
- **Execution Permission**: All Python files must have execution permission.
- **Code Style**: Python scripts should adhere to the PEP 8 coding style. Use `pycodestyle` (version 2.8.*) to check and ensure code style compliance.
- **File Length**: The length of your files will be tested using `wc`.

### Shell Scripts

- **Editor Choices**: You are allowed to use the text editors vi, vim, or emacs for editing the shell scripts.
- **Shell Environment**: All your scripts will be tested on Ubuntu 20.04 LTS.
- **File Ending**: All shell script files should end with a new line.
- **File Length**: Shell scripts should be exactly two lines long (verified by `wc -l file`).
- **Shebang**: The first line of all your files should be exactly `#!/bin/bash`.
- **Execution Permission**: All shell scripts must have execution permission.

### C Scripts

- **Editor Choices**: You are allowed to use the text editors vi, vim, or emacs for editing the C scripts.
- **Compiler**: All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`.
- **File Ending**: All C files should end with a new line.
- **Code Style**: Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`.
- **No Global Variables**: Do not use global variables in your C code.
- **Function Limit**: Each C file should contain no more than 5 functions.
- **Header File**: The prototypes of all functions used in C files must be included in a header file named `lists.h`. Ensure to push your header file to the repository.
- **Include Guard**: All header files must use include guards.
