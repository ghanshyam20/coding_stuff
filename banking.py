
#number guesssing game:
import random

def number_guessing_game():
    secret_number=random.randint(1,1000)
    attempts=0

    while True:
        guess=int(input("Guess the number from 1 to 1000:"))
        attempts+=1
 
        if guess==secret_number:
            print("congrats you won it")

        elif guess<secret_number:
            print("Too low,Try agian")

        else:
            print("Too high.try again.")


if __name__=="__main__":
    number_guessing_game()







