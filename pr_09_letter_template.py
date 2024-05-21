letter = '''\n\nDear <|NAME|>,
Congratulations !!!!!
You are selected in the <|CLG|> college

Date :<|DATE|>
Thank you with Regards !'''

name = input("Enter the Name :")
college = input("Enter College Name :")
date = input("Enter the Date :")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|CLG|>", college)
letter = letter.replace("<|DATE|>", date)

print(letter)