"""Calc brain game.

Player has to calculate values and give his result.
"""
from random import randint, choice
from operator import add, sub, mul

TASK_MSG = 'What is the result of the expression?'


def get_question_answer():
    """Return a question and correct answer"""
    val1, val2 = [randint(1, 100) for _ in range(2)]
    operations = (
        ('+', add),
        ('-', sub),
        ('*', mul)
    )
    operation_name, operation_method = choice(operations)
    question_msg = f'{val1} {operation_name} {val2}'
    result = operation_method(val1, val2)
    return question_msg, str(result)
