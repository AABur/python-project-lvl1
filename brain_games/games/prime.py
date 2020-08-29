"""Prime game logic."""
from random import randint

from pyprimer import is_prime


def game_prime():
    """Even game logic.

    Returns:
        str: task, correct answer
    """
    num = randint(1, 100)
    if is_prime(num):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    task = "{}".format(num)
    return (str(task), str(correct_answer))
