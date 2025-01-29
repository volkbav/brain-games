# file: scripts/brain_even.py
import random


from brain_games.src.my_functions import check_answer
from brain_games.cli import welcome_user


# function to greet user
def greet():
    print('Welcome to the Brain Games!')


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


def main():
    greet()
    game_brain_even()


if __name__ == "__main__":
    main()
