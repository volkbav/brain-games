# import function to generate random numbers
from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# generate random number and check if it is prime
def logic_game():
    number = randint(1, 100)
    count = 0
    divider = 2
    while divider ** 2 <= number and count != 1:
        if number % divider == 0:
            count = 1
        divider += 1
    if count == 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

# print question and return answer and correct answer    
    print(f'Question: {number}')
    answer = input('Your answer: ')
    return (answer, correct_answer)
