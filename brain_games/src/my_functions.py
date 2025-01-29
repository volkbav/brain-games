# check if the answer is correct

def check_answer(answer, correct_answer, user_name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {user_name}!")
        return False
    