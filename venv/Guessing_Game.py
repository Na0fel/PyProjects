
secretWord = "TUTORIAL"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False


while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        if guessCount == 1:
            print("Hint: An issue programmers face")
        if guessCount == 2:
            print("Last Chance!\n Hint: Comes before Hell ")
        guess = input("Enter Your Guess: ").upper()
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("You're out of Guesses!")
else :
    print("You're right!")

