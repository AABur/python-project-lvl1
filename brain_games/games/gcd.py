"""GCD game engine."""

import math
import random

GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."

MIN_NUM = 1
MAX_NUM = 20


def game_engine():
    """GCD game Q&A generation.

    generate two random Numbers
    and calculate greatest common divider for them

    Returns:
        task{str} : Numbers;
        answer{str} : greatest common divider
    """
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    answer = str(math.gcd(num1, num2))
    task = "{} {}".format(num1, num2)
    return (task, answer)
