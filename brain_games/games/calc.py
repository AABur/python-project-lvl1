"""Calc game engine."""

import random
from operator import add, mul, sub

GAME_DESCRIPTION = "What is the result of the expression?"

FUNC_LIST = ((add, '+'), (sub, '-'), (mul, '*'))

MIN_NUM = 1
MAX_NUM = 20


def game_engine():
    """Calc game Q&A generation.

    generate two random numbers
    and calculate result of random operation from list

    Returns:
        task{str} : operation description;
        answer{str} : result of operation
    """
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    operation, symbol = random.choice(FUNC_LIST)
    answer = str(operation(num1, num2))
    task = "{} {} {}".format(num1, symbol, num2)
    return (task, answer)
