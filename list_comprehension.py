
# List Comprehension
numbers = [5, 9, 7, 3, 6, 16, 35, 54, 45, 13, 12, 87, 56, 31, 97, 65, 87, 54, 5]
even = [i for i in numbers if i % 2 == 0]
print(even)

# Set Comprehension
even = {i for i in numbers if i % 2 == 0}
print(even)