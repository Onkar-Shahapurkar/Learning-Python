def r_and_s(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()


str = "         Omi is Good Boy        "
n = r_and_s(str, "Boy")
print("The new String is :" + n)