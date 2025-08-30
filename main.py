"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Monika Mendlíková
email: mendlikova.monika@gmail.com
"""

import random
from typing import List, Tuple

SEP = "-----------------------------------------------"

def welcome() -> None:
    """Prints the welcome message for the Bulls and Cows game."""
    print("Hi there!")
    print(SEP)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEP)


def generate_number(length: int = 4) -> List[str]:
    """
    Generates a random number with unique digits.

    Args:
        length (int): Number of digits to generate. Default is 4.

    Returns:
        List[str]: List of unique digits as strings.
    """
    return random.sample("1234567890", length)


def is_valid_guess(guess: str, length: int = 4) -> bool:
    """
    Validates the player's guess.

    Args:
        guess (str): The player's input.
        length (int): Expected length of the guess. Default is 4.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not guess.isdigit():
        print("Input must contain only digits.")
        return False
    if len(guess) != length:
        print(f"Input must be exactly {length} digits long.")
        return False
    if guess[0] == "0":
        print("Number cannot start with zero.")
        return False
    if len(set(guess)) != length:
        print("Digits must be unique.")
        return False
    return True


def check_guess(secret: List[str], guess: str) -> Tuple[int, int]:
    """
    Compares the secret number with the player's guess.

    Args:
        secret (List[str]): The secret number as a list of digits.
        guess (str): The player's guess as a string.

    Returns:
        Tuple[int, int]: Number of bulls and cows.
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def format_result(bulls: int, cows: int) -> str:
    """
    Formats the result with proper singular/plural for bulls and cows.

    Args:
        bulls (int): Number of bulls.
        cows (int): Number of cows.

    Returns:
        str: Formatted result string.
    """
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_word}, {cows} {cow_word}"


def get_guess(length: int = 4) -> str:
    """
    Prompts the player for a guess until a valid one is entered.

    Args:
        length (int): Expected length of the guess. Default is 4.

    Returns:
        str: Validated player's guess.
    """
    while True:
        guess = input(f"Enter a number:\n{SEP}\n")
        if is_valid_guess(guess, length):
            return guess


def play_game(length: int = 4) -> None:
    """
    Runs the Bulls and Cows game loop.

    Args:
        length (int): Number of digits in the secret number. Default is 4.
    """
    welcome()
    secret = generate_number(length)
    attempts = 0

    print(f"Rules: Guess a {length}-digit number, digits are unique and cannot start with zero.")
    print("A digit in the correct place is a bull.")
    print("A correct digit in the wrong place is a cow.")
    print("Try to guess it!")
    print(SEP)

    while True:
        guess = get_guess(length)
        attempts += 1
        bulls, cows = check_guess(secret, guess)

        if bulls == length:
            print(f"Congratulations! You guessed the number {''.join(secret)} in {attempts} attempts.")
            break
        else:
            print(format_result(bulls, cows))


def main() -> None:
    """Entry point of the game."""
    play_game()


if __name__ == "__main__":
    main()
