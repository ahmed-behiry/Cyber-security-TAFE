#thinking of a number 

#Generate random number 
import random
num= random.randint(1,101)

#Tell user to guess a number, anywhere between 1 – 100 
guess = input("I'm thinking of a number between 1 and 100, guess the number"+"\n")

#Compare input to random number 
while not int(guess) == num:
    if int(guess) > num:
        guess= input("your guess is higher than the number, try again"+"\n")
    else:
        guess= input("your guess is lower than the number, try again"+"\n")

print('congratulations!')

#if correct, print congratulations 

# if not, print too high or too low 