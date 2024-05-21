import functools

l = [45, 98, 8, 87, 65, 82]

val = functools.reduce(max, l)
print(val)