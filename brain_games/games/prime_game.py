"""Prime game.

User has to guess is the number prime or not."""
from random import randint

TASK_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_value_prime(value):
    """Check_is_the"""
    mod = 2
    while mod <= value:
        if value == mod:
            return 'yes'
        elif value % mod == 0:
            return 'no'
        mod += 1


def get_question_answer():
    """Return a question and correct answer"""
    begin = 1
    end = 500
    question_value = randint(begin, end)
    correct_answer = is_value_prime(question_value)

    question_msg = f'{question_value}'
    return question_msg, correct_answer
