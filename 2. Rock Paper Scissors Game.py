import random
import os
import re

def play_check():
    responses=["yes","no"]
    while True:
        try:
            answer = input("Do You want to play: Yes or No")
            if answer.lower() not in responses:
                raise ValueError("Please choose Yes or No only")
            if answer.lower() == "yes":
                return True
            else:
                os.system('cls' if os.name == 'nt' else "Clear")
                print("Okay, see you soon....")
                exit()
        except ValueError as e:
            print(e)


def play_game():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else "Clear")
        print(" ")
        print("Choose: (Rock, Paper, Scissors )")
        choice = input ("R - P - S: ")
        if not re.match("[SsRrPp]",choice):
            print("please choose from [R - P - S]")
            continue

        print(f"Your Choice is {choice}")
        available_choices = ["R","P", "S"]
        comp_choice = random.choice(available_choices)
        print(f"I choose {comp_choice}")

        if comp_choice == choice.upper():
            print("Tie !")
            play = play_check()
        elif comp_choice == "R" and choice.upper()=="S":
            print("hahahaha, Rock beats Scissors, So I win")
            play = play_check()
        elif comp_choice == "S" and choice.upper()=="P":
            print("hahahaha, Scissors beats Paper, So I win")
            play = play_check()
        elif comp_choice == "P" and choice.upper()=="R":
            print("hahahaha, Paper beats Rock, So I win")
            play = play_check()
        else:
            print("Oh no, You win !\n")
            play = play_check()

if __name__ == '__main__':
    play_game()

print("Done")


