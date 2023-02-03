"""Calc brain game.

Player has to calculate values and give his result.
"""
from brain_games.common_core import core_algorithm
from random import randint, choice


def give_task():
    task_msg = 'What is the result of the expression?'
    print(task_msg)


def make_single_calc_game():
    """Create a question for the user and return correct answer"""
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
    print(question_msg)
    return str(result)


def main():
    core_algorithm(give_task, make_single_calc_game)
