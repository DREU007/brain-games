"""Progression game.

User has to give missing value in progression"""
from random import randint

TASK_MSG = 'What number is missing in the progression?'


def get_question_answer():
    """Assign progression, exclude one item.
    Return a question and correct answer."""
    num_items = randint(5, 10)
    step = randint(1, 20)
    start = randint(1, 100)
    finish = start + step * num_items + 1

    progression_list = list(range(start, finish, step))
    missing_item = randint(0, num_items - 1)
    answer = progression_list[missing_item]
    progression_list[missing_item] = '..'

    question_msg = f'{" ".join(progression_list)}'
    return question_msg, answer
