num = int(input("Enter a Number :"))
try:
    c = 1/num
    print(c)
except Exception as e:
    print("You cannot do", e)