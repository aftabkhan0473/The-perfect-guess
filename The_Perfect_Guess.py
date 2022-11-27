import random
randomNumber = random.randint(1,100) # here 1 and 100 both including
guessesNo = 0
a = None # for default define a
while randomNumber != a:
    a = int(input("Enter your guess between 1 to 100 : "))
    if randomNumber == a:
        print("You gusses the right number")
    elif randomNumber>a:
        print("You gusses the wrong number ! please Enter greater number .")
    else:
        print("You gusses the wrong number ! please Enter smaller number .")
    guessesNo += 1

print(f"Congratulation! You guesses the right number in total {guessesNo} guesses")

with open("hiScore.txt", 'r') as f:
    hiScore = int(f.read())
if hiScore > guessesNo:
    print("Congratulation! You have just broken the high score!")
    with open("hiScore.txt", 'w') as f:
        f.write(str(guessesNo))
