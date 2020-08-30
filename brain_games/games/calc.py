"""Calc game engine."""

from operator import add, mul, sub
from random import choice, randint

GAME_DESCRIPTION = "What is the result of the expression?"
FUNC_LIST = ((add, '+'), (sub, '-'), (mul, '*'))
MIN_NUM = 1
MAX_NUM = 20


def game_calc():
    """Calc game Q&A generation.

    generate two random numbers
    and calculate result of random operation from list

    Returns:
        task{str} : operation description;
        answer{str} : result of operation
    """
    num1 = randint(MIN_NUM, MAX_NUM)
    num2 = randint(MIN_NUM, MAX_NUM)
    operation = choice(FUNC_LIST)
    answer = operation[0](num1, num2)
    task = "{} {} {}".format(num1, operation[1], num2)
    return (str(task), str(answer))
