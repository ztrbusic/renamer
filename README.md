# Renamer v0.1

A simple Python script that renames subdirectories of your target directory. Replaces _space_ ( ), _comma_ (,), _dot_ (.), _underscore (_), _triple dash_ (---) and _double dash_ (--) with **single dash** (-).
I used this for my OneDrive batch rename (> 1000 directories). The OneDrive needs to be synced but all files can be set to _available online_, so no need to download anything, just sync directory structure.

## Installation instructions
0. You need to have Python installed on your system (obviously 🤓).
1. Copy the repository somewhere locally, eg. [User]/Documents/python-projects.
2. Open _terminal_ and navigate to the downloaded repository with `cd`.
3. Install virtual environment (venv) with `python -m venv .venv`.
4. Activate your venv with `source .venv/bin/activate`.
5. Install pip with `python3 -m pip install --upgrade pip ` and run `pip install -r requirements.txt to install external modules (just *Unidecode* so far).

## Usage instructions
`python3 renamer-main.py OPTION /path/to/dir`
e.g.: `python3 renamer-main.py read /path/to/dir`

## Options:
- `read` - outputs the list of directories in your given path to a TXT file `renamer-dir-list.txt`
- `execute` - runs the program and renames all of your target directories **recursively**

## Future improvements:
- add _dry-run_ option
- resolve duplicate resulting directory names (currently it won't throw an error, but numbering for the directories of the same name is not working as intended)
- add an option for the user to choose what's gonna be replaced and how
- test the program on Windows