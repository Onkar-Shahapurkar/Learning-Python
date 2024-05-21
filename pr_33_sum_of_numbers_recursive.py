def addition(n):
    if n <= 1:
        return n
    else:
        return n + addition(n-1)


print("The sum of first 16 natural number is :", addition(16))
