#!/usr/bin/env python3
"""This is a script to run brain-games in global environment."""


from sys import stdout

from brain_games.cli import welcome_user


def main():
    """Start brain-games and invite user by asking his name."""
    welcome_msg = 'Welcome to the Brain Games!\n'
    stdout.write(welcome_msg)
    welcome_user()


if __name__ == '__main__':
    main()
