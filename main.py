mport hashlib
from pathlib import Path

def calculate_hash(file_path):
    file_data = Path(file_path).read_bytes()
    file_hash = hashlib.sha256(file_data).hexdigest()
    return file_hash

file_path = "sample.txt"

result = calculate_hash(file_path)

print("File:", file_path)
print("SHA-256:", result)
