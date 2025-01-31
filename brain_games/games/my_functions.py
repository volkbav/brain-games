# import welcome_user function from cli.py
from brain_games.cli import welcome_user


# function to greet user
def greet():
    print('Welcome to the Brain Games!')


# function to check the answer   
def check_answer(answer, correct_answer, user_name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'"
            f"\nLet's try again, {user_name}!")
        return False
 

# function to play the game 
def game(game_name):  
    greet()
    user_name = welcome_user()
    print(f'{game_name.QUESTION}')

# loop to play the game
    for i in range(3):
        answer, correct_answer = game_name.logic_game()
        if check_answer(answer, correct_answer, user_name):
            continue
        else:
            return
    
    print(f'Congratulations, {user_name}!')
