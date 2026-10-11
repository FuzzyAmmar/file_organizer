import shutil
from pathlib import Path


folder_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
}


def organize(folder):

    for f in folder.iterdir():
        if f.is_file():
            category = folder_types.get(f.suffix)
            if category is not None:
                target = folder / category
                target.mkdir(exist_ok=True)
                shutil.move(f, target /f.name)
                print("successfully completed", f.name)
            else:
                print(f.name, "->", "The file is of an unknown type.")


Folder_name = input ("Enter Folder Name?")

folder = Path(Folder_name)


try:
    organize(folder)
except FileNotFoundError:
    print ("The Folder does not exist;check the Name.")

#Organizes Files in a Folder by Type
