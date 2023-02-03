"""Invite user to play brain-games."""
from prompt import string


def welcome_user():
    """Request user to enter his 'name' and return personal welcome msg."""
    name = string('May I have your name? ')
    welcome_reply = (f'Hello, {name}!\n'
                     'Welcome to the Brain Games!')
    print(welcome_reply)
