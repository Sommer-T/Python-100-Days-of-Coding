# Day 12 - Number Guessing Game

import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(guess, answer, attempts_left):
    """Checks the guess against the answer and returns updated attempts."""
    if guess > answer:
        print("Too high.")
        return attempts_left - 1
    elif guess < answer:
        print("Too low.")
        return attempts_left - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return None  # No more attempts needed

def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    attempts = choose_difficulty()

    guess = None

    while attempts and guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer, attempts)

        if attempts is None:
            break

        if attempts == 0:
            print("You've run out of guesses. You lose.")
            return

        print("Guess again.\n")

game()