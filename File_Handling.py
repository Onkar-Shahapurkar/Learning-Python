f = open(f"Files/sample.txt", 'r')
data = f.read()
print(data)
f.close()


print("\n\n")
f = open(f"Files/sample.txt", 'r')
data = f.readline()
print(data)
f.close()


print("\n\n")
f = open(f"Files/sample.txt", 'r')
data = f.readlines()
print(data)
f.close()

'''  Writing to the File
  f = open(f"Files/sample.txt", 'w')
  f.write("Rewrited this content to this file")
  f.close() '''


'''f = open(f"Files/sample.txt", 'a')
f.write("\nAppended this content to this file")
f.close()'''


with open(f"Files/sample.txt") as f:
    print(f.read())