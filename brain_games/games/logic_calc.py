# import function to generate random numbers
import random

QUESTION = 'What is the result of the expression?'

def logic_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    symbol = random.choice(['+', '-', '*'])
    correct_answer = str(eval(f'{number1} {symbol} {number2}'))
    print(f'Question: {number1} {symbol} {number2}')
    answer = input(f'Your answer: ')
    return (answer, correct_answer)        

