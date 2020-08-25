#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user
from brain_games.cli import answer
from brain_games.calc import calc


def main():
    name = welcome_user("What is the result of the expression?")
    i = 1
    while i < 4:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct = calc(num1, num2)
        ans = answer(str(num1) + " ? " + str(num2))
        correct = calc(num1, num2)
        if correct == ans:
            print("Correct!")
        else:
            return print(
                "{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!".format(
                    ans, correct, name
                )
            )
        i += 1
    print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    main()
