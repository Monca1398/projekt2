"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Monika Mendlíková
email: mendlikova.monika@gmail.com
"""

import random

def welcome():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generate_number():
    digits = list("123456789") + ["0"]  # vytvoříme seznam číslic (1–9 + 0)
    random.shuffle(digits)               # zamícháme pořadí
    return digits[:4]   # : = copy        # vezmeme první 4 číslice (budou unikátní)

def check_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))  # porovnáme každou pozici
    cows = sum(g in secret for g in guess) - bulls       # spočítáme, kolik číslic je ve "secret"
                                                          # ale nejsou na správné pozici
    return bulls, cows

def main():
    welcome()
    secret = generate_number()  # skryté číslo, které má hráč uhodnout
    attempts = 0
    print("Hi there! I've generated a 4-digit number with unique digits.")
    print("Try to guess it!")

    while True:  # hlavní herní smyčka – dokud hráč neuhodne
        guess = input("Enter 4 unique digits: ")

        # Kontrola, jestli je vstup validní:
         # - obsahuje jen číslice
          # - má přesně 4 znaky
           # - číslice jsou unikátní
            # - nezačíná nulou
        if not (guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4 and guess[0] != "0"):
            print("Invalid input. Try again.")
            continue

        attempts += 1
        bulls, cows = check_guess(secret, guess)

        if bulls == 4:
            print(f"Correct! You guessed the number {''.join(secret)} in {attempts} attempts.")
            break
        else:
            print(f"{bulls} bulls, {cows} cows")

if __name__ == "__main__":
    main()
