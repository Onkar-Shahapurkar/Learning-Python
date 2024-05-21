
Dict = {
    "pankha": "Fan",
    "vastu": "Item",
    "dabba": "Box",
    "khursi": "Chair"
}

print("Options are :", Dict.keys())
a = input("Enter a Hindi from above options :")
print("The English Translation for your word is :", Dict.get(a))