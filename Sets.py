sets = {56, 65, 89, 3, "Onkar", (54, 89, "Omi"), 65}

print(sets)

# creating empty set and adding values to it
a = set()
a.add(23)
a.add("Omi")
a.add(32)
print(a)

#  Sets Method
print("Length of set :", len(sets))
print("Remove 89 from element :")
sets.remove(89)
print("After Removal of 89 from set :", sets)
print("Using pop method :", sets.pop())
print("Clearing whole set :", a.clear())

print("After union of {3, 11} :", sets.union({3, 11}))

print("After intersection of {3, 11} :", sets.intersection({3, 11}))

sets3 = {8, 3, 4, 89, 9, 32, 11}
print(sets3)