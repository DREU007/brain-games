"""Brain-even game.

A player has to answer 3 times, is number even?
And reply with 'yes' or 'no'."""

from brain_games.common_core import welcome_new_user, user_reply
from random import randint


def is_random_even():
    """Return integer and is it even or not (True/False)."""
    range_start = 1
    range_end = 1_000
    r_number = randint(range_start, range_end)
    is_even = 'yes'
    if r_number % 2:
        is_even = 'no'
    return r_number, is_even


def single_even_game():
    """Print a question with a number and reply to user input."""
    explanation_msg = (
        'Answer "yes" if the number is even, otherwise answer "no".')
    print(explanation_msg)

    number, cor_answer = is_random_even()
    question_msg = f'Question: {number}'
    print(question_msg)
    return cor_answer


def main():
    """Algorithm of program."""
    name = welcome_new_user()
    cycles = 3
    for cycle in range(cycles):
        answer = single_even_game()
        user_reply(answer, name)
    win_msg = f'Congratulations, {name}!'
    print(win_msg)
