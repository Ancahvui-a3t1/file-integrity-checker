import os
import tkinter as tk
from tkinter import filedialog, messagebox
# Assuming database functions can be imported from your backend module
# Adjust the import names below to match your actual functions in database.py / main.py
import database

class FileIntegrityCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(root, text="File Integrity Checker", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=15)

        # Selected File Frame
        self.file_frame = tk.Frame(root)
        self.file_frame.pack(pady=10, fill="x", padx=20)

        self.file_label = tk.Label(self.file_frame, text="Selected File: None", font=("Arial", 10), anchor="w")
        self.file_label.pack(side="left", fill="x", expand=True)

        self.browse_button = tk.Button(self.file_frame, text="Browse", command=self.browse_file, width=10)
        self.browse_button.pack(side="right")

        # Action Buttons Frame
        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=15)

        self.register_button = tk.Button(self.action_frame, text="Register File", command=self.register_file, width=15, bg="#d4edda")
        self.register_button.grid(row=0, column=0, padx=10)

        self.check_button = tk.Button(self.action_frame, text="Check Integrity", command=self.check_integrity, width=15, bg="#d1ecf1")
        self.check_button.grid(row=0, column=1, padx=10)

        # Results / Output Display Box
        self.output_frame = tk.Frame(root)
        self.output_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.output_box = tk.Text(self.output_frame, height=10, font=("Courier", 10), state="disabled", bg="#f8f9fa")
        self.output_box.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.output_frame, command=self.output_box.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.output_box.config(yscrollcommand=self.scrollbar.set)

        # Track selected file path globally in the class
        self.selected_file_path = ""

    def browse_file(self):
        """Opens a file dialog to select a target file."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file_path = file_path
            self.file_label.config(text=f"Selected File: {os.path.basename(file_path)}")
            self.log_message(f"Loaded file path: {file_path}\n")

    def register_file(self):
        """Registers the selected file's SHA-256 hash into the database."""
        if not self.selected_file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return
        
        try:
            # Call your backend function here (e.g., database.register_file(path))
            # Example placeholder logic matching typical implementation:
            database.register_file(self.selected_file_path)
            self.log_message(f"[SUCCESS] Registered: {os.path.basename(self.selected_file_path)}\n")
            messagebox.showinfo("Success", "File successfully registered!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def check_integrity(self):
        """Compares the current file hash against the saved database record."""
        if not self.selected_file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return

        try:
            # Call your backend check function here (e.g., database.check_file(path))
            # Expected to return status like "UNCHANGED" or "MODIFIED"
            status = database.check_file(self.selected_file_path)
            
            if status == "UNCHANGED":
                self.log_message(f"[CHECK] {os.path.basename(self.selected_file_path)}: UNCHANGED (Hashes match)\n", color="green")
            else:
                self.log_message(f"[CHECK] {os.path.basename(self.selected_file_path)}: MODIFIED (Hashes differ!)\n", color="red")
        except Exception as e:
            messagebox.showerror("Check Error", str(e))

    def log_message(self, message, color="black"):
        """Appends messages to the text output box safely."""
        self.output_box.config(state="normal")
        self.output_box.insert(tk.END, message)
        self.output_box.see(tk.END)
        self.output_box.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileIntegrityCheckerApp(root)
    root.mainloop()
