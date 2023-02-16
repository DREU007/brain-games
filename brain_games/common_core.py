"""This module has common part for all games."""
from prompt import string
from sys import exit


def run_game(game_task, get_game_question_answer):
    """Algorithm of program."""
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(
        f"Hello, {user_name}!\n"
        f"{game_task}"
    )

    cycles_count = 3
    # num_cycles = 3
    for cycle in range(cycles_count):
        question, correct_answer = get_game_question_answer()
        print(f'Question: {question}')

        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            exit()

    print(f'Congratulations, {user_name}!')
