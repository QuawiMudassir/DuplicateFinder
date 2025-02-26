import os
import hashlib

def calculate_hash(file_path, chunk_size=4096):
    """Calculates the hash of a file."""
    hash_func = hashlib.md5()  # You can use sha256 for more security
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def find_duplicates(directory):
    """Scans the directory and returns a list of duplicate file groups."""
    file_hashes = {}  # Dictionary to store file hashes
    duplicates = []   # List to store lists of duplicate files

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  # Get full file path
            file_hash = calculate_hash(file_path)  # ✅ Use file_path instead of file.path

            if file_hash:
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = [file_path]

    # Collect duplicates
    for paths in file_hashes.values():
        if len(paths) > 1:
            duplicates.append(paths)  # ✅ Append to the list

    return duplicates
