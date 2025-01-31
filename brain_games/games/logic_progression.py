# import function to generate random numbers
from random import randint

QUESTION = 'What number is missing in the progression?'


def logic_game():
    progression = []
    step = randint(1, 10)
    start = randint(1, 100)
    hiden_number_index = randint(0, 9)
# generate progression and save correct answer
    for i in range(10):
        progression.append(start + step * i)
        if i == hiden_number_index:
            correct_answer = str(progression[i])
            progression[i] = '..'

# print question and return answer and correct answer    
    print(f'Question: {" ".join(map(str, progression))}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

