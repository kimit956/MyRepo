# Should play 3 rounds of rock, paper, scissors
import random  # must import random because random does not come with python library

name = input("What is your name?\n")
win = 0
lose = 0
game_round = 1
computer = random.randint(1,4)  # Random integer from 1 to 3 (inclusive)

while game_round <= 3:
    user = int(input("For rock enter 1.\nFor paper enter 2.\nFor scissors enter 3.\nWhat is your choice? "))
    if computer == 1:
        if user == 1:
            print("\nBoth the computer and " + name + " throw rock.\nIt's a tie!\n")
        elif user == 2:
            print("\nThe computer throws rock.\n" + name + " throws paper.\n" + name + " wins this round!\n")
            win = win + 1
        elif user == 3:
            print("\nThe computer throws rock.\n" + name + " throws scissors.\n" + name + " loses this round.\n")
            lose = lose + 1
        else:
            print("\nYou did not enter a correct command, please try again.\n")

    elif computer == 2:
        if user == 1:
            print("\nThe computer throws paper.\n" + name + " throws rock.\n" + name + " loses this round.\n")
            lose = lose + 1
        elif user == 2:
            print("\nBoth the computer and " + name + " throw paper.\nIt's a tie!\n")

        elif user == 3:
            print("\nThe computer throws paper.\n" + name + " throws scissors.\n" + name + " wins this round!\n")
            win = win + 1
            break
        else:
            print("\nYou did not enter a correct command, please try again.\n")
    elif computer == 3:
        if user == 1:
            print("\nThe computer throws scissors.\n" + name + " throws rock.\n" + name + " wins this round!\n")
            win = win + 1
            break
        elif user == 2:
            print("\nThe computer throws scissors.\n" + name + " throws paper.\n" + name + " loses this round.\n")
            lose = lose + 1
            break
        elif user == 3:
            print("\nBoth the computer and " + name + " throw scissors.\nIt's a tie!\n")
            break
        else:
            print("\nYou did not enter a correct command, please try again.\n")
    game_round = game_round + 1  # advances the game round

if win > lose:
    print(name + " wins the game!")
elif lose > win:
    print(name + " loses the game.")
else:
    print("Round " + game_round + "\nWins " + str(win) + " Loses " + str(lose) + "\nIt's a tie!")


