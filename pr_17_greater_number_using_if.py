num1 = int(input("enter Number 1 :"))
num2 = int(input("enter Number 2 :"))
num3 = int(input("enter Number 3 :"))
num4 = int(input("enter Number 4 :"))

if num1 > num4:
    f1 = num1
else:
    f1 = num4

if num2 > num3:
    f2 = num2
else:
    f2 = num3

if f1 > f2:
    print("Greater number from above input is :", f1)
else:
    print("Greater number from above input is :", f2)