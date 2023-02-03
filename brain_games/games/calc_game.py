"""Calc brain game.

Player has to calculate values and give his result.
"""
from random import randint, choice


def give_task():
    """Return task for a user."""
    task_msg = 'What is the result of the expression?'
    return task_msg


def assign_question_answer():
    """Return a question and correct answer"""
    val1, val2 = [randint(1, 100) for _ in range(2)]
    available_operators = ['*', '+', '-']
    operator = choice(available_operators)
    if operator == '*':
        result = val1 * val2
    elif operator == '+':
        result = val1 + val2
    else:
        result = val1 - val2

    question_msg = f'Question: {val1} {operator} {val2}'
    return question_msg, str(result)
