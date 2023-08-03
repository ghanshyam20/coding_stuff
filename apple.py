#small project on 
import random

def choice():
    while True:
        user_choice=input("Enter your choice rock or scissor or paper.").lower()
        if user_choice in ['rock','paper','scissor']:
            return user_choice
        else:
            print("Invalid choice ..try again....")



def play_rps():
    choices=['rock','paper','scissor']
    computer_choice=random.choice(choices)
    user_choice=choice()

    print(f"computer choose:{computer_choice}")
    if user_choice==computer_choice:
        print("its equal or tie")

    elif (user_choice=='rock' and computer_choice=='scissor'):
        print("congrats you win!!!")

    elif(user_choice=='paper' and computer_choice=='rock'):
        print("congrats you win!!!")

    elif (user_choice=='scissor' and computer_choice=='paper'):
        print("congrats you win!!!")
       

   
     
    else:
        print("computer wins!!")


if __name__=="__main__":
    play_rps()


