
import random
# import welcome_user function from cli.py
from brain_games.cli import welcome_user


def check_answer(answer, correct_answer, user_name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {user_name}!")
        return False
# ---------------------------------------------- 

# Game logic
# ----------------------------------------------    

# function to check if the number is even

def game_brain_even():
    user_name = welcome_user()
#    print(f'user_name = {user_name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
# set answer and correct_answer to empty string to enter the loop
    answer = ''
    correct_answer = ''
    for i in range(3):
        number = random.randint(1, 100)
        answer = input(f'Question: {number}\nYour answer: ')        
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if check_answer(answer, correct_answer, user_name):
            continue
        else:
            return
    print(f'Congratulations, {user_name}!')
# ---------------------------------------------- 
