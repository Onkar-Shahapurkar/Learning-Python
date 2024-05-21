with open(f"Files/poem.txt") as f:
    content = f.read()

with open(f"Files/copy.txt", 'w') as f:
    f.write(content)