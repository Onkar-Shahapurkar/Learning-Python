import random


randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter Your Guess :"))
    guesses += 1
    if userGuess == randNumber:
        print("Your Guess is Right !!!!")
    else:
        if userGuess > randNumber:
            print("Wrong !, Enter a Smaller Number")
        else:
            print("Wrong !, Enter a Larger Number")

print(f"You guessed the Number in {guesses} guesses")
with open("Files/hiscore_of_guess_game.txt", "r") as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("Congratulations !!! You broke the previous record")
    with open("Files/hiscore_of_guess_game.txt", "w") as f:
        f.write(str(guesses))