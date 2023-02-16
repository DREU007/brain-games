"""Brain-even game.

A player has to answer is number even?
And reply with 'yes' or 'no'."""
from random import randint

TASK_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    """Return a question and correct answer"""
    number = randint(1, 1000)

    question_msg = f'{number}'
    answer = 'no' if number % 2 else 'yes'
    return question_msg, answer
