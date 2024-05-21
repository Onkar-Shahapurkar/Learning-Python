num = input("Enter a Number :")
try:
    num = int(num)
    c = 1 / num
    print(c)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except:
    print("An error occurred")
