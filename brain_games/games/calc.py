"""Calc game logic."""
# + add
# - sub
# * mul
# TODO - refactor if-elif-else

from random import choice, randint


def game_calc():
    """Calc game logic.

    Returns:
        str: task, correct answer
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    oper = choice("+-*")
    if oper == "+":
        correct_answer = num1 + num2
    elif oper == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    task = "{} {} {}".format(num1, oper, num2)
    return (str(task), str(correct_answer))
