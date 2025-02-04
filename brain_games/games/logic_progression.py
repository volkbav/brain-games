from random import randint

QUESTION = 'What number is missing in the progression?'
START_RANGE = 1
END_RANGE = 100
START_STEP = 1
END_STEP = 10
START_HIDEN_NUMBER = 0
END_HIDEN_NUMBER = 9
COUNT_OF_PROGRESSION = 10


def logic_game():
    progression = []
    step = randint(START_STEP, END_STEP)
    start = randint(START_RANGE, END_RANGE)
    hiden_number_index = randint(START_HIDEN_NUMBER, END_HIDEN_NUMBER)
# generate progression and save correct answer
    for i in range(COUNT_OF_PROGRESSION):
        progression.append(start + step * i)
        if i == hiden_number_index:
            correct_answer = str(progression[i])
            progression[i] = '..'

# print question and return answer and correct answer    
    print(f'Question: {" ".join(map(str, progression))}')
    answer = input('Your answer: ')
    return (answer, correct_answer)        

