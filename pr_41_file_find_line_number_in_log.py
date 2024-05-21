content = True
i = 1

with open(f"Files/log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content, end="")
            print("Yes python is present")
            print(i, "\n")
        i = i+1