import random
attempts = []

def score():
    if not attempts :
        print("There is no high score")
    else:
        print(f'The current high score is {min(attempts)} attempts')

def game():
    atts = 0
    rand_num = random.randint(1,10)
    play_or_not = input("Do you want to play? Yes or No:")
    if play_or_not.lower() != "yes":
        print("Ok, as you like")
        exit()
    else:
        score()
    while play_or_not.lower()=="yes":
        try:
            guess=int(input("Guess a number between 1 and 10:"))
            if guess < 1 or guess >10:
                raise ValueError("Please guess a number between the given range")

            atts+=1
            attempts.append(atts)

            if guess == rand_num:
                print("Bravooooo!")
                print(f'it tooks you {atts} attempts')

                play_or_not = input("Do you want to play again? Yes or No:")
                if play_or_not.lower() != "yes":
                    print("Ok, See you soon....")
                    break

                else:
                    atts=0
                    rand_num = random.randint(1,10)
                    score()
                    continue
            else:
                if guess > rand_num:
                    print("oops, lower than your guess")
                elif guess < rand_num:
                    print("oops, greater than your guess")

        except ValueError as e:
            print("oh no! that is not a valid number, please try again.... ")
            print(e)

if __name__ == '__main__':
    game()
print("Done")