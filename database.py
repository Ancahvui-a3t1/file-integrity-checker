import sqlite3

DATABASE = "integrity.db"


def create_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS file_records (
            file_path TEXT PRIMARY KEY,
            sha256_hash TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            content = file.read()
            sha256.update(content)

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    return sha256.hexdigest()

def register_file(file_path):
    file_hash = calculate_hash(file_path)

    if file_hash is None:
        return

    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
    "INSERT OR IGNORE INTO file_records (file_path, sha256_hash) VALUES (?, ?)",
    (file_path, file_hash)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 1:
         print("File registered successfully!")
    else:
         print("File is already registered.")

def check_file(file_path):
    current_hash = calculate_hash(file_path)
    if current_hash is None:
        return
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "SELECT sha256_hash FROM file_records WHERE file_path = ?",
        (file_path,)
    )

    record = cursor.fetchone()
    connection.close()

    if record is None:
        print("File is not registered.")
        return

    saved_hash = record[0]

    if current_hash == saved_hash:
        print("STATUS: UNCHANGED")
    else:
        print("STATUS: MODIFIED")


def list_registered_files():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        "SELECT file_path, sha256_hash FROM file_records"
    )

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No files registered yet.")
        return

    print("\n===== Registered Files =====")

    for file_path, saved_hash in records:
        print(f"File: {file_path}")
        print(f"SHA-256: {saved_hash}")
        print("-" * 40)


if __name__ == "__main__":
    create_database()

    while True:
        print("\n===== File Integrity Checker =====")
        print("1. Register a file")
        print("2. Check file integrity")
        print("3. List all registered files")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter file path: ")
            register_file(file_path)

        elif choice == "2":
            file_path = input("Enter file path: ")
            check_file(file_path)

        elif choice == "3":
            list_registered_files()

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
