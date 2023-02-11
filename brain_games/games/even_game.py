"""Brain-even game.

A player has to answer is number even?
And reply with 'yes' or 'no'."""
from random import randint

TASK_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    """Return a question and correct answer"""
    start, finish = 1, 1_000
    number = randint(start, finish)
    question_msg = f'{number}'
    answer = 'no' if question_msg % 2 else 'yes'
    return question_msg, answer
