import random

num = random.randint(1,5) #generate random number between 1 and 5

def numberGuess(num):
    guess = input("Guess a number between 1 and 5 (Integers Only)")
    guessint = int(guess) #convert input to int
    if guessint == num: #win condition
        print("You Win!")
    elif guessint > num:
        print("Too high!")
        numberGuess(num)
    elif guessint < num:
        print("Too low!")
        numberGuess(num)

numberGuess(num)
