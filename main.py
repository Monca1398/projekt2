"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Monika Mendlíková
email: mendlikova.monika@gmail.com
"""

sep = "-----------------------------------------------"

import random
from typing import List, Tuple


def welcome() -> None:
    """Prints the welcome message for the Bulls and Cows game."""
    print("Hi there!")
    print(sep)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a Bulls and Cows game.")
    print(sep)


def generate_number() -> List[str]:
    """
    Generates a random 4-digit number with unique digits.

    Returns:
        List[str]: A list of 4 unique digits as strings.
    """
    # random.sample selects 4 unique elements directly
    return random.sample("1234567890", 4)


def check_guess(secret: List[str], guess: str) -> Tuple[int, int]:
    """
    Compares the secret number with the player's guess.

    Args:
        secret (List[str]): The secret number as a list of single-digit strings.
        guess (str): The player's guess as a 4-digit string.

    Returns:
        Tuple[int, int]: A tuple (bulls, cows) where:
            bulls (int): Number of digits correct and in the correct position.
            cows (int): Number of digits correct but in the wrong position.
    """
    bulls: int = sum(s == g for s, g in zip(secret, guess))
    cows: int = sum(g in secret for g in guess) - bulls
    return bulls, cows


def main() -> None:
    """
    Main game loop for Bulls and Cows.

    Handles:
        - Displaying welcome message.
        - Generating secret number.
        - Validating player input.
        - Counting attempts.
        - Displaying bulls and cows after each guess.
        - Ending the game when the player guesses correctly.
    """
    welcome()
    secret: List[str] = generate_number()
    attempts: int = 0

    print("Rules: Guess a 4-digit number, digits are unique and cannot start with zero.")
    print("A digit in the correct place is a bull.")
    print("A correct digit in the wrong place is a cow.")
    print("Try to guess it!")
    print(sep)

    while True:
        guess: str = input("Enter 4 unique digits: ")

        # Input validation
        if not guess.isdigit():
            print("Input must contain only digits.")
            continue
        if len(guess) != 4:
            print("Input must be exactly 4 digits long.")
            continue
        if guess[0] == "0":
            print("Number cannot start with zero.")
            continue
        if len(set(guess)) != 4:
            print("Digits must be unique.")
            continue

        attempts += 1
        bulls, cows = check_guess(secret, guess)

        if bulls == 4:
            print(f"Congratulations! You guessed the number {''.join(secret)} in {attempts} attempts.")
            break
        else:
            print(f"{bulls} bulls, {cows} cows")


if __name__ == "__main__":
    main()
