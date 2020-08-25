#!/usr/bin/env python3

import random

from brain_games.cli import answer, welcome_user
from brain_games.even import even


def main():
    name = welcome_user('Answer "yes" if number even otherwise answer "no".')
    i = 1
    while i < 4:
        num = random.randint(1, 100)
        ans = answer(num)
        correct = even(num)
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
