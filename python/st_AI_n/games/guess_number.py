import random
import os

def guess_number():
    random_number = random.randint(0, 100)
    guesses = 0
    game_started = True

    os.system("cls")

    while True:
        if game_started:
            try:
                user_guess = int(input("Guess a number between 1 and 100: "))
            except ValueError:
                os.system("cls")
                print("enter a number dumbass")
                continue

            if user_guess == random_number:
                os.system("cls")
                print("You guessed correctly!\nnow go kill yourself")
                print(f"it took you {guesses} guesses")
                break
            elif user_guess < random_number:
                os.system("cls")
                print("imagine guessing too low lmao")
                guesses += 1
            elif user_guess > random_number:
                os.system("cls")
                print("imagine guessing too high lmao")
                guesses += 1
