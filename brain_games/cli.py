import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

# function to greet user
def greet():
    print('Welcome to the Brain Games!')