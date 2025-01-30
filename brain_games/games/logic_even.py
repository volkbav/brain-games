import random
# import welcome_user function from cli.py
from brain_games.cli import welcome_user


def game_brain_even():
    user_name = welcome_user()
#    print(f'user_name = {user_name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
# set answer and correct_answer to empty string to enter the loop
    answer = ''
    correct_answer = ''