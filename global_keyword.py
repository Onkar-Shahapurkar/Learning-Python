a = 54

def func1():
    global a
    print(a)
    a = 8
    print("Value changed of global attribute 'a' to :", a)


func1()
print("Now the value of the global attribute will be :", a)