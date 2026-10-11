# file_organizer

A Python script that sorts the files in a folder by type.

## What it does
Organizes a messy folder by moving each file into a folder that matches its type.

## How it works
It reads each file's extension and moves it to a dedicated folder:
images go to `Images`, documents go to `Documents`, and videos go to `Videos`.

## How to run
Type `python organizer.py`, press Enter, then type the folder name.

## Notes
- Files with unknown extensions are left in place, and their names are printed.
- If the folder does not exist, a clear message is shown instead of an error.
