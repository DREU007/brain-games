"""Prime game.

User has to guess is the number prime or not."""
from brain_games.common_core import core_algorithm
from random import randint


def game_instruction():
    invite_msg = (
        'Answer "yes" if given number is prime. Otherwise answer "no".')
    print(invite_msg)


def is_value_prime(value):
    """Check_is_the"""
    mod = 2
    while mod <= value:
        if value == mod:
            return 'yes'
        elif value % mod == 0:
            return 'no'
        mod += 1


def prime_single_game():
    """Invite user to answer a question, return correct result."""
    begin = 1
    end = 500
    question_value = randint(begin, end)
    correct_answer = is_value_prime(question_value)

    question_msg = f'Question: {question_value}'
    print(question_msg)
    return correct_answer


def main():
    """Start prime game."""
    core_algorithm(game_instruction, prime_single_game)
