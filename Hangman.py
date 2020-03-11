import random


words = open("C:/Users/eheambh/PycharmProjects/Melbourne_Poly/food.txt").readlines()
myword = random.choice(words).strip("\n")
print(myword)
char_lst = list(myword)
trials = 10
blanks_lst = ["_" for i in char_lst]
guess = input("Computer has a food related word consist of "+str(len(char_lst))+" letters, can you guess it?"+"\n"+"you have 10 trials to guess the letters, what is your first guess?"+"\n"+str(blanks_lst)+"\n"+str(trials)+" Trials left"+"\n")

for k in range(trials-1):
    if guess in myword:
        while guess in blanks_lst:
            guess=input("You guessed that before, enter new guess"+"\n")
        for i,char in enumerate(char_lst):
            if guess == char:
                blanks_lst[i]=guess
        if "_" not in blanks_lst:
            break
        guess=input("good guess"+"\n"+str(blanks_lst)+"\n"+str(trials-1-k)+" Trials left"+"\n")
    else:
        guess=input("bad guess"+"\n"+str(blanks_lst)+"\n"+str(trials-1-k)+" Trials left"+"\n")


if "_" in blanks_lst:
    print("out of trials, you lose!")
else:
    print(myword+" is the correct word, you won!")
