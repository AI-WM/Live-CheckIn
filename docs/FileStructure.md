# File Structure

This file contains the file structure for this project and can be used as the guidance of where to put/find a file.

## Structure

```
/
|-- demo/
    |-- *.py
    `-- *.ipynb
|-- docs/
    |-- img/
    |   |-- *.png
    |   `-- *.jpg
    |-- CONTRIBUTING.md
    `-- FileSturcture.md
|-- src/
    `-- *.py
|-- README.md
|-- requirements.txt
`-- LICENSE
```

## Detail Information

### demo

This directory holds the quick demo, running scripts and running examples that can give the user an idea of how to start and how to use this project.

### docs

This directory includes the relative documentation for this project. Documents are usually under `.md` and `.txt` format.

### src

This directory is for source code only. The files under this directory need to be tested and using `.py` format only.

### other files

#### README.md

This document contains:
* What the project does
* Why the project is useful
* How users can get started with the project
* Where users can get help with your project
* Who maintains and contributes to the project
* ...

#### requirements.txt

List packages needed for this project. 

Can be used to install required packages by the following command:
```bash
pip install -r requirements.txt
```

#### LICENSE

The open source license for this project.
