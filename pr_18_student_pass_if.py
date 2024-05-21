num1 = int(input("Enter Subject  Marks :"))
num2 = int(input("Enter Subject 2 Marks :"))
num3 = int(input("Enter Subject 3 Marks :"))
num4 = int(input("Enter Subject 4 Marks :"))

if num1 < 33 or num3 < 33 or num2 < 33 or num4 < 33:
    print("You are fail")
elif (num4 + num3 + num1 + num2)/4 < 40:
    print("You are Fail")
else:
    print("Congratulations you are Pass")