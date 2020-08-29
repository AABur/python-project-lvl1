"""GCD game engine."""

from math import gcd
from random import randint

GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 20


def game_gcd():
    """GCD game Q&A generation.

    generate two random Numbers
    and calculate greatest common divider

    Returns:
        task{str} : two Numbers;
        answer{str} : greatest common divider
    """
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    correct_answer = gcd(num1, num2)
    task = "{} {}".format(num1, num2)
    return (str(task), str(correct_answer))
