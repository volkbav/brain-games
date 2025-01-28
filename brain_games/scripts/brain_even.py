# file: scripts/brain_even.py
import random

from brain_games.cli import welcome_user


# function to greet user
def greet():
    print('Welcome to the Brain Games!')


# function to check if the number is even
def brain_even():
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
# check if the answer is correct
        if answer == correct_answer:
            print('Correct!')
            continue
        elif answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


def main():
    greet()
    brain_even()


if __name__ == "__main__":
    main()
