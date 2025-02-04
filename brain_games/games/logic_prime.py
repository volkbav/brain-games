from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
END_RANGE = 100


# generate random number and check if it is prime
def logic_game():
    number = randint(START_RANGE, END_RANGE)
    count = 0
    divider = 2
    DEGREE = 2
    while divider ** DEGREE <= number:
        if number % divider == 0:
            count = 1
            break
        divider += 1
    if count == 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

# print question and return answer and correct answer    
    print(f'Question: {number}')
    answer = input('Your answer: ')
    return (answer, correct_answer)
