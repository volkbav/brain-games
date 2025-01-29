# file: scripts/brain_even.py
# ----------------------------------------------

# import game logic from my_functions.py
from brain_games.src.my_functions import game_brain_even
# ----------------------------------------------

# import the function to greet the user
from brain_games.cli import greet
# ----------------------------------------------

def main():
    greet()
    game_brain_even()


if __name__ == "__main__":
    main()
