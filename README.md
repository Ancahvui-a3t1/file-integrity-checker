# File Integrity Checker

## About the Project
File Integrity Checker is a beginner-friendly Python project that detects changes in files using SHA-256 hashing.

It stores each registered file's original hash in an SQLite database and compares it with the current hash to determine whether the file has been modified.

## Features
- Register files and save their SHA-256 hashes.
- Check whether a file has changed.
- List all registered files and their saved hashes.
- Handle missing files.
- Prevent duplicate file registrations.
- Use a simple menu-driven interface.

## Technologies Used
- **Python** — application logic
- **hashlib** — SHA-256 hashing
- **SQLite** — storing file paths and hashes

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run the application:

   `python3 database.py`

4. Choose an option from the menu.

## How It Works
1. Register a file to calculate and save its SHA-256 hash.
2. Check the file to calculate its current hash.
3. Compare the current hash with the saved hash.
4. Display `UNCHANGED` if the hashes match or `MODIFIED` if they differ.

## Project Status
Beginner project — currently implemented as a command-line application.
