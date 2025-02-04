from math import gcd
from random import randint

QUESTION = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def logic_game():
    number1 = randint(START_RANGE, END_RANGE)
    number2 = randint(START_RANGE, END_RANGE)
    correct_answer = str(gcd(number1, number2))
    print(f'Question: {number1} {number2}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

