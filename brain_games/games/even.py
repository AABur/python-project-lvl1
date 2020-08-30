"""Even game logic."""
from random import randint

GAME_DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'."
MIN_NUM = 1
MAX_NUM = 20
YES_NO = ("yes", "no")


def game_even():
    """Even game Q&A generation.

    generate random Number and check if a Number is Even

    Returns:
        task{str} : Number;
        answer{str} : Even status
    """
    num = randint(MIN_NUM, MAX_NUM)
    answer = YES_NO[num % 2]
    task = "{}".format(num)
    return (task, answer)
