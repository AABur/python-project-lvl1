"""Progression game logic."""

from random import randint

GAME_DESCRIPTION = "What number is missing in the progression?"
START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 10
PROGERSSION_LENGTH = 10


def game_progression():
    """Progression game Q&A generation.

    It forms an arithmetic progression,
    replacing one of the numbers with two points.

    Returns:
        task{str} : arithmetic progression;
        answer{str} : hidden number
    """
    start = randint(START_MIN, START_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    a_progression = [(start + (ind * step))
                     for ind in range(PROGERSSION_LENGTH)]
    hidden = randint(1, PROGERSSION_LENGTH)
    answer = str(a_progression[hidden - 1])
    a_progression[hidden - 1] = ".."
    task = " ".join(str(ind) for ind in a_progression)
    return (task, answer)
