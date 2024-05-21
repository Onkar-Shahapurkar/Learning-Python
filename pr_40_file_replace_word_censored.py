

with open(f"Files/sample.txt") as f:
    content = f.read()
    content = content.replace('Donkey', "$#$%@$%@")
with open(f"Files/sample.txt", 'w') as f:
    f.write(content)


list = ["mote", "bc", "mc", "yedya"]
for word in list:
    content = content.replace(word, "$#$%@$%@")
    with open(f"Files/sample.txt", 'w') as f:
        f.write(content)