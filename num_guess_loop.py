#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : April 2025
# Guesses a number between 0-9 in a loop until you get it

import random

random_numb = random.randint(0, 9)

while True:
    user_numb_guess = input("guess a number between (0-9): ")

    try:
        user_numb_guess_int = int(user_numb_guess)

        if user_numb_guess_int < 0 or user_numb_guess_int > 9:
            print(f"{user_numb_guess_int} is not between 0 and 9")
        elif user_numb_guess_int == random_numb:
            print(f"{user_numb_guess_int} is the correct guess!!!")
            break
        else:
            print("bad guess, try harder")
    except Exception:
        print(f"{user_numb_guess} is not an integer")

print("Thanks for playing")
