# file: scripts/brain_games.py
from brain_games.cli import welcome_user

# import greeting from my_functions.py
from brain_games.games.my_functions import greet
# ----------------------------------------------


def main():
    greet()
    welcome_user()


if __name__ == "__main__":
    main()
