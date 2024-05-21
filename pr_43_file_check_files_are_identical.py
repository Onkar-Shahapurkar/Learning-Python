with open(f"Files/poem.txt") as f:
    f1 = f.read()

with open(f"Files/sample.txt") as f:
    f2 = f.read()

if f1 == f2:
    print("Two Files are Identical")
else:
    print("Two Files are not Identical")