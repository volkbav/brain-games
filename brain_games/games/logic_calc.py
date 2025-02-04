from random import choice, randint

QUESTION = 'What is the result of the expression?'
START_RANGE = 1
END_RANGE = 100


def logic_game():
    number1 = randint(START_RANGE, END_RANGE)
    number2 = randint(START_RANGE, END_RANGE)
    symbol = choice(['+', '-', '*'])
    correct_answer = str(eval(f'{number1} {symbol} {number2}'))
    print(f'Question: {number1} {symbol} {number2}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

