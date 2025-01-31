# import function to generate random numbers
import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# generate random number and ask user if it is even
def logic_game():
    number = random.randint(1, 100)
    answer = input(f'Question: {number}\nYour answer: ')

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (answer, correct_answer)       

