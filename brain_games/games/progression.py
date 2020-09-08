"""Progression game engine."""

import random

GAME_DESCRIPTION = "What number is missing in the progression?"

START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 10
PROGERSSION_LENGTH = 10


def get_task():
    """Progression game Q&A generation.

    It forms an arithmetic progression,
    replacing one of the numbers with two points.

    Returns:
        task{str} : arithmetic progression;
        answer{str} : hidden number
    """
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = [(start + (ind * step))
                   for ind in range(PROGERSSION_LENGTH)]
    hidden_element_index = random.randint(0, PROGERSSION_LENGTH - 1)
    answer = str(progression[hidden_element_index])
    progression[hidden_element_index] = ".."
    task = " ".join(str(ind) for ind in progression)
    return (task, answer)
