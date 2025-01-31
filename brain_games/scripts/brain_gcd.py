# file: scripts/brain_gcd.py

# import module to start the game
from brain_games.games import logic_gcd

# import function from my_functions.py
from brain_games.games.my_functions import game

# ----------------------------------------------


def main():
    game(logic_gcd)


if __name__ == "__main__":
    main()
