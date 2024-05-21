def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good Omi")


a = increment("hj")
print(a)