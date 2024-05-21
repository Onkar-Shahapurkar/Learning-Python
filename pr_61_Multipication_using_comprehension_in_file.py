num = int(input("Enter a Number :"))

table = [num * i for i in range(1, 11)]

print(table)

with open("Files/Multiplication_using_list_comprehension.txt", 'a') as f:
    f.write(str(table))
    f.write('\n')