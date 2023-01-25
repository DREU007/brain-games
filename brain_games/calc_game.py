"""Calc brain game.

Player has to calculate values and give his result.
"""
from brain_games.common_core import core_algorithm
from random import randint, choice


def single_calc_game():
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
    invite_msg = ('What is the result of the expression?\n'
                  f'Question: {val1} {operator} {val2}')
    print(invite_msg)
    return str(result)


def main():
    core_algorithm(single_calc_game)
