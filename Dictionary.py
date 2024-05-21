
Dict = {
    "key": "Value",
    "omi": "Student",
    "list": "[2, 68, 'Onkar']",
    "secondDict": {'pusshy': 'Friend'}
}

print(Dict)
print("Value of List :", Dict['list'])  # access using []
print("Value of Key :", Dict['key'])
print("Dictionary into Dictionary :", Dict['secondDict'])
print("Dictionary of Dictionary Value :", Dict['secondDict']['pusshy'])
anotherDict = {
    "sam": "Friend"
}

#  Dictionary Methods

print(Dict.items())  # print key-value pairs
print(Dict.keys())  # print keys
print(Dict.values())  # print values
print(Dict.get('omi'))  # access using get method
print(Dict.get('something'))  # access to unavailable key using get method
Dict.update({"trupti": "Friend"})  # adding pair to the Dictionary
Dict.update(anotherDict)
print(Dict)
