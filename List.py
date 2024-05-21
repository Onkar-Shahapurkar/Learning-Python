a = ["Onkar", "Omi", 4, True, 5]

print(a)

print(a[1])

print(a[0:2])

print(a[-5:3])

#  Sorting Methods
b = [5, 8, 3, 4, 58, 32, 89]

print("Original String :", b)

b.append(46)
print("Appended String :", b)

b.insert(3, 98)
print("Inserted String :", b)

b.sort()
print("Sorted String :", b)

b.reverse()
print("Reversed String :", b)

print("Popped at Index 2 :", b.pop(2))

b.remove(89)
print("Removed 89 from String :", b)