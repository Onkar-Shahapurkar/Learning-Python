num = int(input("Enter a Number :"))
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False
        break
    else:
        prime = True

if prime:
    print("The Entered number is Prime Number")
else:
    print("The Entered number is not a Prime Number")