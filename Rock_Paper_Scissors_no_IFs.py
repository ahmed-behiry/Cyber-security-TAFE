import random

# game words list
game = ["Rock", "Paper", "Scissors"]

# choose randomly between 0,1,2
num = random.randint(0, 2)

comp_choice = game[num]

user_choice = input(
    "what is your move?" + "\n" + "Enter R for Rock" + "\n" + "Enter P for Paper" + "\n" + "Enter S for Scissors" + "\n")

result_dic = {"Rock_R": "it is draw!", "Rock_P": "you win!", "Rock_S": "you lose!", "Paper_R": "you lose!", "Paper_P": "it is draw!", "Paper_S": "you win!", "Scissors_R": "you win!", "Scissors_P": "you lose!", "Scissors_S": "it is draw!"}

print("My choice was "+comp_choice)
print(result_dic[comp_choice+"_"+user_choice])
