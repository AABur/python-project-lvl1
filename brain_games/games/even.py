"""Even game logic."""
from random import randint

GAME_DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'."
MIN_NUM = 1
MAX_NUM = 20


def game_even():
    """Even game Q&A generation.

    generate random Number and check if a Number is Even

    Returns:
        task{str} : Number;
        answer{str} : Even status
    """
    num = randint(MIN_NUM, MAX_NUM)
    answer = ("yes", "no")
    correct_answer = answer[num % 2]
    task = "{}".format(num)
    return (str(task), str(correct_answer))
