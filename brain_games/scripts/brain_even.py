#!/usr/bin/env python3
"""Script to run brain-even in global environment."""
from brain_games.common_core import run_game
from brain_games.games.even_game import give_task, assign_question_answer


def main():
    run_game(give_task, assign_question_answer)


if __name__ == '__main__':
    main()
