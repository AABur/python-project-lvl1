"""Command line interface (only for brain_games.py)."""

import prompt


def welcome_user():
    """Welcome dialog."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
