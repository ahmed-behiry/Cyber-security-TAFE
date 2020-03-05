import random

#game words list
game = ["Rock", "Paper", "Scissors"]

#choose randomly between 0,1,2
num = random.randint(0,2)

comp_choice = game[num]

user_choice = input("what is your move?"+"\n"+"Enter R for Rock"+"\n"+"Enter P for Paper"+"\n"+"Enter S for Scissors"+"\n")

if user_choice == "R":
    if comp_choice=="Rock":
        print("my choice was "+comp_choice+"\n"+"it is draw!")
    elif comp_choice=="Paper":
        print("my choice was "+comp_choice+"\n"+"you lose!")
    elif comp_choice == "Scissors":
        print("my choice was "+comp_choice+"\n"+"you win!")       
elif user_choice == "P":
    if comp_choice=="Rock":
        print("my choice was "+comp_choice+"\n"+"you win!")
    elif comp_choice=="Paper":
        print("my choice was "+comp_choice+"\n"+"it is draw!")
    elif comp_choice=="Scissors":
        print("my choice was "+comp_choice+"\n"+"you lose!")
elif user_choice == "S":
    if comp_choice=="Rock":
        print("my choice was "+comp_choice+"\n"+"you lose!")
    elif comp_choice=="Paper":
        print("my choice was "+comp_choice+"\n"+"you win!")
    elif comp_choice=="Scissors":
        print("my choice was "+comp_choice+"\n"+"it is draw!")
else:
    print("wrong input!")
    
    
