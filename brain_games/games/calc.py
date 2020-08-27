    """Game logic."""
from random import randint, choice


def game_calc():
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
    return (task, correct_answer)
