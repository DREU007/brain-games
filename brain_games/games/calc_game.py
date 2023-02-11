"""Calc brain game.

Player has to calculate values and give his result.
"""
from random import randint, choice

TASK_MSG = 'What is the result of the expression?'


def get_question_answer():
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

    question_msg = f'{val1} {operator} {val2}'
    return question_msg, str(result)
