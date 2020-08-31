"""Progression game logic."""

from random import randint

GAME_DESCRIPTION = "What number is missing in the progression?"
SATRT_MIN_MAX = (1, 20)  # arithmetic progression first number
STEP_MIN_MAX = (1, 10)  # arithmetic progression step
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
    a_progression = [(start + (ind * step)) for ind in range(NUMBER)]
    hidden = randint(1, NUMBER)
    answer = str(a_progression[hidden - 1])
    a_progression[hidden - 1] = ".."
    task = ' '.join(str(ind) for ind in a_progression)
    return (task, answer)
