import os
from scanner import find_duplicates
from remover import delete_duplicates, move_duplicates

def main():
    directory = input("Enter the directory to scan for duplicates: ").strip()

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    duplicates = find_duplicates(directory)

    if not duplicates:
        print("No duplicates found.")
        return
    print("\nDuplicates files found:")
    for i, files in enumerate(duplicates, 1):
        print(f"\nSet {i}:")
        for file in files:
            print(f" {file}")

    action = input("\nDo you want to (d)elete or (m)ove duplicates? (d/m)").strip().lower()

    if action == 'd':
        delete_duplicates(duplicates)
    elif action == 'm':
        destination = input("Enter the destination folder: ").strip()
        move_duplicates(duplicates, destination)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()



