#!/usr/bin/env python3
"""Brain-even game.

A player has to answer 3 times, is number even?
And reply with 'yes' or 'no'."""

from sys import exit
from prompt import string
from random import randint


def welcome_user():
    """Print a welcome msg to user, request his name and return user_name."""
    welcome_msg = 'Welcome to the Brain Games!'
    print(welcome_msg)
    name = string('May I have your name? ')
    welcome_reply = f'Hello, {name}!\n'
    explanation_msg = (
        'Answer "yes" if the number is even, otherwise answer "no".')
    print(welcome_reply + explanation_msg)
    return name


def is_random_even():
    """Return integer and is it even or not (True/False)."""
    range_start = 1
    range_end = 1_000
    r_number = randint(range_start, range_end)
    is_even = 'yes'
    if r_number % 2:
        is_even = 'no'
    return r_number, is_even


def single_game(name):
    """Print a question with a number and reply to user input."""
    number, is_even = is_random_even()

    question_msg = f'Question: {number}'
    print(question_msg)
    user_answer = string('Your answer: ')

    if user_answer == is_even:
        print('Correct!')
    else:
        wrong_msg = (
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{is_even}'.\n"
            f"Let's try again, {name}!")
        print(wrong_msg)
        exit()


def main():
    """Algorithm of program."""
    name = welcome_user()
    cycles = 3
    for cycle in range(cycles):
        single_game(name)
    win_msg = f'Congratulations, {name}!\n'
    print(win_msg)


if __name__ == '__main__':
    main()
