"""Brain-even game.

A player has to answer is number even?
And reply with 'yes' or 'no'."""
from random import randint

TASK_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_number_and_is_it_even(range_start=1, range_finish=1_000):
    """Return integer and is it even or not (True/False)."""
    number = randint(range_start, range_finish)
    answer_is_even = 'yes'
    if number % 2:
        answer_is_even = 'no'
    return number, answer_is_even


def get_question_answer():
    """Return a question and correct answer"""
    number, cor_answer = create_number_and_is_it_even()
    question_msg = f'{number}'
    return question_msg, cor_answer
