numbers = [5, 9, 7, 3, 6, 16, 35, 54, 45, 13, 12, 87, 56, 31, 97, 65, 87, 54, 5]

for index, i in enumerate(numbers):
    if index == 2 or index == 4 or index == 6:
        print(f"The value at {index+1}th element is {i}")