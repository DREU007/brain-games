"""This module has common part for all games."""
from prompt import string
from sys import exit


def welcome_new_user():
    """Print a welcome msg to user, request his name and return user_name."""
    welcome_msg = 'Welcome to the Brain Games!'
    print(welcome_msg)
    name = string('May I have your name? ')
    welcome_reply = f'Hello, {name}!'
    print(welcome_reply)
    return name


def user_reply(correct_answer, user_name):
    """Check correct_answer with user_answer.

    Print msg if True or False and exit.
    """
    user_answer = string('Your answer: ')
    if user_answer == correct_answer:
        print('Correct!')
    else:
        wrong_msg = (
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\n"
            f"Let's try again, {user_name}!")
        print(wrong_msg)
        exit()
