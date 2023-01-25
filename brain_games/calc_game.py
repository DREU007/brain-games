"""Calc brain game.

Player has to calculate values and give his answer.
"""
from brain_games.common_core import welcome_new_user, user_reply

def single_calc_game():
    """Create a question for the user and return correct answer"""



def main():
    name = welcome_new_user()
    cycles = 3
    for cycle in range(cycles):
        answer = single_calc_game()
        user_reply(answer, name)
