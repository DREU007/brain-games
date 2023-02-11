"""Prime game.

User has to guess is the number prime or not."""
from random import randint

TASK_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_value_prime(value):
    """Check is the value prime?"""
    mod = 2
    while mod <= value:
        if value == mod:
            return True
        elif value % mod == 0:
            return False
        mod += 1
    return False


def get_question_answer():
    """Return a question and correct answer"""
    begin = 1
    end = 500
    value = randint(begin, end)
    question_msg = f'{value}'
    answer = 'yes' if is_value_prime(value) else 'no'

    return question_msg, answer
