# import function to generate random numbers
import random

# import welcome_user function from cli.py
from brain_games.cli import welcome_user

# import function from my_functions.py
from brain_games.games.my_functions import greet
from brain_games.games.my_functions import check_answer

# generate random number and ask user if it is even
def logic_even():
    number = random.randint(1, 100)
    answer = input(f'Question: {number}\nYour answer: ')
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (answer, correct_answer)       


def game_brain_even():
    greet()
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        answer, correct_answer = logic_even()
        if check_answer(answer, correct_answer, user_name):
            continue
        else:
            return
    print(f'Congratulations, {user_name}!')

