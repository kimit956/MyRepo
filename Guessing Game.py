import random

attemptsLeft = 5
playAgain = True
while attemptsLeft != 0 & playAgain:  # keeps asking while user still has attempts left or user wants to play again
    randNum = random.randint(1,101)  # generates a random integer from 1 to 100 (inclusive)

    try:  # will make sure that the guess is not a decimal or letter
        guess = int(input("Enter a guess: "))
        guess1 = int(guess)
        attemptsLeft -= 1
    except ValueError:
        attemptsLeft -= 1
        guess1 = int(input("Must be between 1 and 100: "))

    while guess1 < 1 or guess1 > 100:  # entered a number lower than 1 or higher than 100 or is not an integer
        attemptsLeft -= 1
        guess1 = int(input("Must be between 1 and 100: "))

    while guess1 != randNum:
        if guess1 < randNum:  # guessed too low
            attemptsLeft -= 1
            guess1 = int(input("Too low.  Guess higher: "))

        elif guess1 > randNum:  # guessed too high
            attemptsLeft -= 1
            guess1 = int(input("Too high. Guess lower: "))

        if guess1 == randNum or attemptsLeft == 0:  # runs if user guesses correct number or has 0 attempts left
            if guess1 == randNum:  # if the user guesses correctly
                print("\nYOU WIN!")
            elif attemptsLeft == 0:  # if the user ran out of attempts
                print("\nRan out of attempts, the number was", randNum, ". YOU LOSE!")

            asks = input("Do you want to play again? ")  # asks the user if he/she wants to play again
            if asks.lower() == "y" or asks.lower() == "yes":
                playAgain = True
            else:
                break  # stops the while loop

