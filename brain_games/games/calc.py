"""Calc game logic"""
# + add
# - sub
# * mul
# TODO - refactor if-elif-else

from random import randint, choice


def game_calc():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    oper = choice("+-*")
    if oper == "+":
        correct_answer = num1 + num2
    elif oper == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    task = "{} {} {}".format(num1, oper, num2)
    return (str(task), str(correct_answer))
