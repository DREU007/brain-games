"""This module has common part for all games."""
from prompt import string
from sys import exit


def core_algorithm(game_task, assign_game_question_answer):
    """Algorithm of program."""
    welcome_msg = 'Welcome to the Brain Games!'
    print(welcome_msg)

    user_name = string('May I have your name? ')
    welcome_reply = f'Hello, {user_name}!'
    print(welcome_reply)

    # print(game_task)
    game_task()

    num_cycles = 3
    for cycle in range(num_cycles):
        # question, correct_answer = assign_game_question_answer()
        # print(question)
        correct_answer = assign_game_question_answer()

        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')

        else:
            wrong_msg = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!")
            print(wrong_msg)
            exit()

    win_msg = f'Congratulations, {user_name}!'
    print(win_msg)
