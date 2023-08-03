#this is class for the function.
#we will do the small project using python function for dice....

#dice ma total 6 wota part hunxa ...
#import random le random module import garxa which is buil-in python module. it is used to generate random numbers.

#mini project for the dice roll ..


import random

def roll_dice():
    return random.randint(1,6)



def dice_rolling_simulator():
    while True:
        input("please enter to roll the dice....")
        result=roll_dice()
        print(f"You rolled a {result} ")


        again=input("do you want to roll again ?(y or n)")
        if again.lower()!='y':
            break



if __name__=="__main__":
    dice_rolling_simulator()






