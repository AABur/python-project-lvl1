"""Prime game engine."""

import random

import pyprimer

GAME_DESCRIPTION = "Answer 'yes' if number prime otherwise answer 'no'."

MIN_NUM = 1
MAX_NUM = 20


def game_engine():
    """Prime game Q&A generation.

    generate random Number and check if a Number is Prime

    Returns:
        task{str} : Number;
        answer{str} : Prime status
    """
    num = random.randint(MIN_NUM, MAX_NUM)
    answer = "yes" if pyprimer.is_prime(num) else "no"
    task = "{}".format(num)
    return (task, answer)
