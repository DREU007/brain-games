"""Greatest common divider game.

User has to give his answer what is the greatest common divider
for the two random given integers."""
from random import randint

TASK_MSG = 'Find the greatest common divisor of given numbers.'


def get_highest_divider_for(a, b):
    """Checking for highest common divider for values (a, b) and return it."""
    for divider in range(min(a, b), 0, -1):
        if a % divider == 0 and b % divider == 0:
            return divider


def get_question_answer():
    """Return a question and correct answer"""
    val1 = randint(1, 100)
    val2 = randint(1, 100)

    question_msg = f'{val1} {val2}'
    answer = get_highest_divider_for(val1, val2)
    return question_msg, str(answer)
