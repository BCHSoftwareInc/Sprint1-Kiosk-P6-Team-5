import random

secret = random.randint(1,100)
count = 1 
guess = int(input("enter a number from 1 to 100: "))
while guess != secret:
    if guess > secret:
        print ("too high.")
    else:
        print ("too low.")
    guess = int(input("enter a number from 1 to 100: "))
    count = count + 1

print ("congrats you needed " + str(count) + " gusses.")