# import function to generate random numbers
import random

# import welcome_user function from cli.py
from brain_games.cli import welcome_user

# import function from my_functions.py
from brain_games.games.my_functions import greet
from brain_games.games.my_functions import check_answer



#function to calculate the expression
def game_brain_calc():
    user_name = welcome_user()
    print('What is the result of the expression?')
    # set answer and correct_answer to empty string to enter the loop
    answer = ''
    correct_answer = ''
    for i in range(3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        symbol = random.choice(['+', '-', '*'])
        correct_answer = str(eval(f'{number1} {symbol} {number2}'))
        print(f'Question: {number1} {symbol} {number2}')
        answer = input(f'Your answer: ')
        if check_answer(answer, correct_answer, user_name):
            continue
        else:
            return
    print(f'Congratulations, {user_name}!')