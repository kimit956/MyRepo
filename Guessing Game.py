import random

attemptsLeft = 5
playAgain = True
while((attemptsLeft != 0) & (playAgain == True)): #keeps asking while user still has attempts left or user wants to play again
    randNum = random.randint(1,101) #generates a random integer
    try: #will make sure that the guess is not a decimal or letter
        guess = int(input("Enter a guess: "))
        guess1 = int(guess)
        attemptsLeft -= 1
    except ValueError:
        attemptsLeft -= 1
        guess1 = int(input("Must be between 1 and 100: "))


    while (guess1 < 1 or guess1 > 100): #entered a number lower than 1 or higher than 100 or is not an integer
        attemptsLeft -= 1
        guess1 = int(input("Must be between 1 and 100: "))


    while(guess1 != randNum):
        if (guess1 < randNum): #guessed too low
            attemptsLeft -= 1
            guess1 = int(input("Too low.  Guess higher: "))

        elif (guess1 > randNum): #guessed too high
            attemptsLeft -= 1
            guess1 = int(input("Too high. Guess lower: "))

        if (guess1 == randNum):
            print("YOU WIN!") #victory message
            playAgain = bool(input("Do you want to play again? "))
            if (playAgain == "Yes"):
                playAgain = True
            else:
                playAgain = False

        if (attemptsLeft == 0): #Ran out of attempts
            print("Ran out of attempts, the number was", randNum, ". YOU LOSE!")
            playAgain = bool(input("Do you want to play again?"))
            if (playAgain == "Y" or playAgain == "y"):
                playAgain = True
            else:
                break #stops the while loop
