"""Progression game logic."""
# TODO - too many local variables
from random import randint


def game_progression():
    """Progression game logic.

    Returns:
        str: task, correct answer
    """
    strt = randint(1, 10)
    stp = randint(1, 10)
    hdn = randint(1, 10)
    cnt = 10
    lst = [strt]
    for _ in range(cnt - 1):
        lst.append(lst[-1] + stp)
    correct_answer = lst[hdn - 1]
    lst[hdn - 1] = ".."
    task = "{}".format(lst)
    return (str(task), str(correct_answer))
