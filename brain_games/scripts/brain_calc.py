#!/usr/bin/env python3
"""Script to run brain_game.calc_game.py."""
from brain_games.common_core import run_game
from brain_games.games.calc_game import give_task, assign_question_answer


def main():
    run_game(give_task, assign_question_answer)


if __name__ == '__main__':
    main()
