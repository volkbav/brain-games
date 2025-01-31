# import function to generate random numbers
from random import choice, randint

QUESTION = 'What is the result of the expression?'


def logic_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    symbol = choice(['+', '-', '*'])
    correct_answer = str(eval(f'{number1} {symbol} {number2}'))
    print(f'Question: {number1} {symbol} {number2}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

