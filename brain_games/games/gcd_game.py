"""Greatest common divider game.

User has to give his answer what is the greatest common divider
for the two random given integers."""
from random import randint

TASK_MSG = 'Find the greatest common divisor of given numbers.'


def prepare_values():
    """Prepare data for a question, return a, b values and correct answer."""
    a, b = [randint(1, 100) for _ in range(2)]
    for divider in range(min(a, b), 0, -1):
        if a % divider == 0 and b % divider == 0:
            return a, b, divider


def get_question_answer():
    """Return a question and correct answer"""
    val1, val2, answer = prepare_values()

    question_msg = f'{val1} {val2}'
    return question_msg, str(answer)
