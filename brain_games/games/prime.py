"""Prime game logic."""

from random import randint

from pyprimer import is_prime

GAME_DESCRIPTION = "Answer 'yes' if number prime otherwise answer 'no'."

MIN_NUM = 1
MAX_NUM = 20
YES_NO = ("yes", "no")


def game_prime():
    """Prime game Q&A generation.

    generate random Number and check if a Number is Prime

    Returns:
        task{str} : Number;
        answer{str} : Prime status
    """
    num = randint(MIN_NUM, MAX_NUM)
    answer = YES_NO[not is_prime(num)]
    task = "{}".format(num)
    return (str(task), str(answer))
