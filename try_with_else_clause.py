try:
    i = int(input("Enter a Number :"))
    c = 1/i
    print(c)
except Exception as e:
    print(e)
else:
    print("Code Run Succesfully")  # Execute only if try block executed successfully