import os

with open(f"Files/copy.txt") as f:
    content = f.read()

with open(f"Files/renamed_by_python.txt", 'w') as f:
    f.write(content)

os.remove(f"Files/copy.txt")