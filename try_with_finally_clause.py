try:
    i = int(input("Enter a Number :"))
    c = 1/i
    print(c)
except Exception as e:
    print(e)
    exit()
finally:
    print("We are Done")  # Will always Execute no matter what happens