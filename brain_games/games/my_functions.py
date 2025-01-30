# function to use in games

# import function to generate random numbers
import random
# import welcome_user function from cli.py
from brain_games.cli import welcome_user

# function to greet user
def greet():
    print('Welcome to the Brain Games!')


# function to check the answer   
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
 
