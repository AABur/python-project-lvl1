"""Even game logic."""
# TODO - refactor while-if-if-break
from random import randint


def game_gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = num2
    while correct_answer > 0:
        if not num1 % correct_answer:
            if not num2 % correct_answer:
                break
        correct_answer -= 1
    task = "{} {}".format(num1, num2)
    return (str(task), str(correct_answer))
