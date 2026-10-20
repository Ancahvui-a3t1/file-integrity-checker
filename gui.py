import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main window
root = tk.Tk()
root.title("File Integrity Checker")
root.geometry("400x300")

# Label at the top
title_label = tk.Label(root, text="File Integrity Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Function placeholders for our buttons
def register_file():
    # We will connect this to database.py later!
    filename = filedialog.askopenfilename()
    if filename:
        messagebox.showinfo("Success", f"Selected: {filename}")

def check_file():
    filename = filedialog.askopenfilename()
    if filename:
        messagebox.showinfo("Checked", f"Checked file: {filename}")

# Create buttons
btn_register = tk.Button(root, text="Register New File", width=25, command=register_file)
btn_register.pack(pady=10)

btn_check = tk.Button(root, text="Check File Integrity", width=25, command=check_file)
btn_check.pack(pady=10)

# Start the application loop
root.mainloop()
