def func():
    print("This is a Function")


func()


def greet(name="User"):
    print(f"Hello, {name}")


str1 = "Onkar"
greet(str1)
greet("Omi")
greet()


def add(num1, num2):
    return num1 + num2


addition = add(54, 21)
print("Addition of two numbers is :", addition)