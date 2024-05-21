def openFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"File {filename} does not Exist")


openFile("Files/File1.txt")
openFile("Files/File2.txt")
openFile("Files/File3.txt")