import os
import hashlib

def calculate_hash(file_path):
    """Returns the SHA256 hash of the file"""
    hashsha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hashsha256.update(chunk)
    except Exception as e:
        print(f"error reading {file_path}: {e}")
        return None
    return hashsha256.hexdigest()

def find_duplicates(directory):
    """Scans the directory and returns a dictionary of duplicate files."""
    file_hashes={}
    duplicates = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file )
            file_hash = calculate_hash(file.path)

            if file_hash:
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = [file_path]

    #Collect duplicate
    for paths in file_hashes.values():
        if len(paths)>1:
            duplicates.append(paths)

    return duplicates

