"""Progression game logic."""

from random import randint

GAME_DESCRIPTION = "What number is missing in the progression?"
SATRT_MIN_MAX = (1, 20)  # arithmetic progression first number
STEP_MIN_MAX = (1, 5)  # arithmetic progression step
NUMBER = 10  # arithmetic progression length


def game_progression():
    """Progression game Q&A generation.

    It forms an arithmetic progression,
    replacing one of the numbers with two points.

    Returns:
        task{str} : arithmetic progression;
        answer{str} : hidden number
    """
    start = randint(SATRT_MIN_MAX[0], SATRT_MIN_MAX[1])
    step = randint(STEP_MIN_MAX[0], STEP_MIN_MAX[1])
    # arithmetic progression
    a_progression = list(range(start, start + step * NUMBER, step))
    # hidden number
    answer = str(a_progression[randint(1, NUMBER) - 1])
    # convert list to string and remove symbols , [ ]
    task = "{}".format(a_progression).replace(",", "")[1:-1]
    # replace hidden number for '..'
    task = task.replace(answer, "..")
    return (task, answer)
