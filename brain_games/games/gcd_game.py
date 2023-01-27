"""Greatest common divider game.

User has to give his answer what is the greatest common divider
for the two random given integers."""

from brain_games.common_core import core_algorithm
from random import randint


def game_instruction():
    invite_msg = 'Find the greatest common divisor of given numbers.'
    print(invite_msg)


def prepare_values():
    """Prepare data for a question, return a, b values and correct answer."""
    a, b = [randint(1, 100) for _ in range(2)]
    for divider in range(min(a, b), 0, -1):
        if a % divider == 0 and b % divider == 0:
            return a, b, divider


def gcd_single_game():
    """Prepare question for a user and return correct answer."""
    val1, val2, answer = prepare_values()

    question_msg = f'Question: {val1} {val2}'
    print(question_msg)
    return str(answer)


def main():
    """Start gcd game."""
    core_algorithm(game_instruction, gcd_single_game)
