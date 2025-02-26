import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedStyle
from scanner import find_duplicates
from remover import delete_duplicates, move_duplicates

class DuplicateFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Duplicate File Finder")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Apply theme
        style = ThemedStyle(root)
        style.set_theme("arc")  # Options: "breeze", "arc", "plastik", etc.

        # Frame for folder selection
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill=tk.X)

        ttk.Label(frame, text="Select a directory to scan:", font=("Arial", 12)).pack(anchor="w")

        self.folder_path = tk.StringVar()
        self.folder_entry = ttk.Entry(frame, textvariable=self.folder_path, width=60)
        self.folder_entry.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Button(frame, text="Browse", command=self.browse_folder).pack(side=tk.RIGHT, padx=5)

        # Scan button
        ttk.Button(root, text="Scan for Duplicates", command=self.scan, style="TButton").pack(pady=10)

        # Listbox with Scrollbar
        self.list_frame = ttk.Frame(root, padding=10)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.list_frame, width=90, height=15, font=("Arial", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Action buttons
        button_frame = ttk.Frame(root, padding=10)
        button_frame.pack(fill=tk.X)

        self.delete_button = ttk.Button(button_frame, text="Delete Duplicates", command=self.delete_duplicates, state=tk.DISABLED)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

        self.move_button = ttk.Button(button_frame, text="Move Duplicates", command=self.move_duplicates, state=tk.DISABLED)
        self.move_button.pack(side=tk.RIGHT, padx=5, pady=5, expand=True)

        self.duplicates = []

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def scan(self):
        directory = self.folder_path.get()
        if not directory:
            messagebox.showwarning("Warning", "Please select a folder!")
            return

        self.duplicates = find_duplicates(directory)
        self.listbox.delete(0, tk.END)

        if not self.duplicates:
            messagebox.showinfo("Result", "No duplicate files found.")
            return

        for i, files in enumerate(self.duplicates, 1):
            self.listbox.insert(tk.END, f"Set {i}:")
            for file in files:
                self.listbox.insert(tk.END, f"  {file}")

        self.delete_button.config(state=tk.NORMAL)
        self.move_button.config(state=tk.NORMAL)

    def delete_duplicates(self):
        delete_duplicates(self.duplicates)
        messagebox.showinfo("Success", "Duplicates deleted successfully!")
        self.scan()

    def move_duplicates(self):
        destination_folder = filedialog.askdirectory()
        if not destination_folder:
            return

        move_duplicates(self.duplicates, destination_folder)
        messagebox.showinfo("Success", f"Duplicates moved to {destination_folder}")
        self.scan()

if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicateFinderApp(root)
    root.mainloop()
