# LAB - Class 19

## Project: Automation

## Author: Bradley Hower

By automating tasks, greater efficiency can be achieved. Here there are five automation created.

To input directories/folders, the directory is entered in reference to the current directory of the run. For example, if ran from downloads, `assets/user-docs` would specify a the subfolder "user-docs" within the assets folder.

1. Create a folder - Creates a folders as named.
2. Moved User Files - Moves files of a deleted user to a new temp folder. Old folder is eliminated.
3. Document Sort - Sorts log and email documents to self-described folders.
4. Log and Warning Parse - Parses a log file into two files, warnings, and errors.
5. Backup - Creates a backup of a provided folder. Creates a new folder as described, copying new files thereto.

## Run

To run the application, `python3 automation.py`

Requires the following installtion via `pip install <name>`:

- `Console`
- `Prompt`
- `os`
- `shutil`
- `re`
