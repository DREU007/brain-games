"""Brain-even game.

A player has to answer 3 times, is number even?
And reply with 'yes' or 'no'."""

from brain_games.common_core import core_algorithm
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
    number, cor_answer = is_random_even()
    invite_msg = (
        'Answer "yes" if the number is even, otherwise answer "no".'
        f'Question: {number}')
    print(invite_msg)
    return cor_answer


def main():
    """Algorithm of program."""
    core_algorithm(single_even_game())
