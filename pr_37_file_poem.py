with open(f"Files/poem.txt") as f:
    content = f.read()

if 'Twinkle' in content:
    print("The File contains the word Twinkle")
else:
    print("The File does not contain the word Twinkle")