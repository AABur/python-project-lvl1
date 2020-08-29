"""Even game logic."""
from random import randint


def game_even():
    """Even game logic.

    Returns:
        str: task, correct answer
    """
    num = randint(1, 100)
    answer = ("yes", "no")
    correct_answer = answer[num % 2]
    task = "{}".format(num)
    return (str(task), str(correct_answer))
