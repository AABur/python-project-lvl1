"""Even game engine."""

import random

GAME_DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'."

MIN_NUM = 1
MAX_NUM = 20


def game_engine():
    """Even game Q&A generation.

    generate random Number and check if a Number is Even

    Returns:
        task{str} : Number;
        answer{str} : Even status
    """
    num = random.randint(MIN_NUM, MAX_NUM)
    answer = "no" if num % 2 else "yes"
    task = "{}".format(num)
    return (task, answer)
