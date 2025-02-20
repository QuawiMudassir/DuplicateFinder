import os
import shutil

def delete_duplicates(duplicates):
    """Delete Duplicate files, keep the first one"""
    for files in duplicates:
        for file in files[1:]:
            try:
                os.remove(file)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

def move_duplicates(duplicates, destination_folder):
    """Moves duplicate files to a destination folder"""
    if not os.path.exists(destination_folder):
        os.makdirs(destination_folder)

    for files in duplicates:
        for file in files[1:]:
            try:
                shutil.move(file, os.path.join(destination_folder, os.path.basename(file)))
                print(f"Moved: {file} → {destination_folder} ")
            except Exception as e:
                print(f"Error moving {file}: {e}")
