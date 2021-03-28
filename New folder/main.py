
import random
print("number guessing game")
n = random.randint(0,10)
s = int(input("enter a number between 1 to 10: "))
chances = 0

print("Guess a number (between 1 and 9):")


while chances < 5:


    guess = int(input("Enter your guess:- "))



    if guess == n:

        print("Congratulation YOU WON!!!")
        break


    elif guess < n:
        print("Your guess was too low: Guess a number higher than", guess)


    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1



if not chances < 5:
    print("YOU LOSE!!! The number is", n)