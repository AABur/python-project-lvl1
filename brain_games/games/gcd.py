"""GCD game logic."""


from math import gcd
from random import randint


def game_gcd():
    """GCD game logic.

    Returns:
        str: task, correct answer
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = gcd(num1, num2)
    task = "{} {}".format(num1, num2)
    return (str(task), str(correct_answer))
