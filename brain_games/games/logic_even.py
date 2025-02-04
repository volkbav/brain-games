from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


# generate random number and ask user if it is even
def logic_game():
    number = randint(START_RANGE, END_RANGE)
    answer = input(f'Question: {number}\nYour answer: ')

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (answer, correct_answer)       

