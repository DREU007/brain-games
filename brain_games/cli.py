"""Invite user to play brain-games."""
from sys import stdout

from prompt import string


def welcome_user():
    """Request user to enter his 'name' and return personal welcome msg."""
    name = string('May I have your name? ')
    welcome_reply = 'Hello, {0}!\n'.format(name)
    stdout.write(welcome_reply)
