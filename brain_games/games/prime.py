"""Prime game engine."""

from random import randint

from pyprimer import is_prime

GAME_DESCRIPTION = "Answer 'yes' if number prime otherwise answer 'no'."

MIN_NUM = 1
MAX_NUM = 20


def run_prime():
    """Prime game Q&A generation.

    generate random Number and check if a Number is Prime

    Returns:
        task{str} : Number;
        answer{str} : Prime status
    """
    num = randint(MIN_NUM, MAX_NUM)
    answer = "yes" if is_prime(num) else "no"
    task = "{}".format(num)
    return (task, answer)
