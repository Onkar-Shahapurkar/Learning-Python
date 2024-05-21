a = int(input("Enter Number a :"))
b = int(input("Enter Number b :"))
try:
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("Infinite")