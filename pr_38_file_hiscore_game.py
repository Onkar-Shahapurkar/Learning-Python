def game():
    return 2


score = game()
with open(f"Files/hiscore.txt") as f:
    hiscore = f.read()

if hiscore == '':
    with open(f"Files/hiscore.txt", 'w') as f:
        f.write(str(score))
elif int(hiscore) < score:
    with open(f"Files/hiscore.txt", 'w') as f:
        f.write(str(score))
    print("Highscore Changed")