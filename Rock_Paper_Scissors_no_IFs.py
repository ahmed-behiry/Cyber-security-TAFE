import random
game = ["Rock", "Paper", "Scissors"]
result_dic = {"Rock_R": "it is draw!", "Rock_P": "you win!", "Rock_S": "you lose!",
              "Paper_R": "you lose!", "Paper_P": "it is draw!", "Paper_S": "you win!",
              "Scissors_R": "you win!", "Scissors_P": "you lose!", "Scissors_S": "it is draw!",
              "Rock_r": "it is draw!", "Rock_p": "you win!", "Rock_s": "you lose!",
              "Paper_r": "you lose!", "Paper_p": "it is draw!", "Paper_s": "you win!",
              "Scissors_r": "you win!", "Scissors_p": "you lose!", "Scissors_s": "it is draw!"}
again = "Y"
while again in ["Y","y"]:
    num = random.randint(0, 2)
    comp_choice = game[num]

    user_choice = input(
        "what is your move?" + "\n" + "Enter R for Rock" + "\n" + "Enter P for Paper" + "\n" + "Enter S for Scissors" + "\n")

    while user_choice not in ["R","P","S","r","p","s"]:
        user_choice = input(
            "invalid choice" + "\n" + "Enter R for Rock" + "\n" + "Enter P for Paper" + "\n" + "Enter S for Scissors" + "\n")
    print("My choice was "+comp_choice)
    print(result_dic[comp_choice+"_"+user_choice])
    again = input("do you want to play again?"+"\n" + "Enter Y for Yes" + "\n" + "Enter N for No"+ "\n")
    while again not in ["Y","N","y","n"]:
        again = input("invalid choice"+"\n" + "Enter Y for Yes" + "\n" + "Enter N for No"+ "\n")
