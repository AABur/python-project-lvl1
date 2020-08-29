"""Brain Games Engine."""

from brain_games.cli import (
    congratulations,
    correct,
    qa_dialog,
    welcome_dialog,
    wrong_answer,
)

STEPS = 3  # number of game steps


def run_game(game_name, game_description):
    """Brain Games Engine.

    Executing game process

    Args:
        game_name (function): game logic module
        game_description (str): game rules
    """
    user_name = welcome_dialog(game_description)
    for _ in range(STEPS):
        (game_task, game_answer) = game_name()
        user_answer = qa_dialog(game_task)
        if user_answer != game_answer:
            wrong_answer(user_answer, game_answer, user_name)
            return
        correct()
    congratulations(user_name)
