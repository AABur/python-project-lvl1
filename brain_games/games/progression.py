"""Progression game logic."""

from random import randint

GAME_DESCRIPTION = "What number is missing in the progression?"
STP_MIN_MAX = (1, 5)  # arithmetic progression step
FST_MIN_MAX = (1, 20)  # arithmetic progression first number
NUMBER = 10  # arithmetic progression length


def game_progression():
    """Progression game Q&A generation.

    It forms an arithmetic progression,
    replacing one of the numbers with two points.

    Returns:
        task{str} : arithmetic progression;
        answer{str} : hidden number
    """
    step = randint(STP_MIN_MAX[0], STP_MIN_MAX[1])
    hidden = randint(FST_MIN_MAX[0], FST_MIN_MAX[1])
    a_progression = [randint(1, 10)]
    for _ in range(NUMBER - 1):
        a_progression.append(a_progression[-1] + step)
    answer = a_progression[hidden - 1]
    a_progression[hidden - 1] = ".."
    task = "{}".format(a_progression)
    return (str(task), str(answer))
