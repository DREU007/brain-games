"""Progression game.

User has to give missing value in progression"""
from random import randint


def give_task():
    """Return task for a user."""
    task_msg = 'What number is missing in the progression?'
    return task_msg


def assign_question_answer():
    """Assign progression, exclude one item.
    Return a question and correct answer."""
    num_items = randint(5, 10)
    start_psn = randint(1, 100)
    step = randint(1, 20)
    progression_list = [
        str(start_psn + item * step) for item in range(num_items)]
    missing_item = randint(0, num_items - 1)
    answer = progression_list[missing_item]
    progression_list[missing_item] = '..'

    question_msg = f'Question: {" ".join(progression_list)}'
    return question_msg, answer
