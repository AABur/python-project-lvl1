"""Brain Games Engine."""

from brain_games.cli import (
    congratulations,
    correct,
    qa_dialog,
    welcome_dialog,
    wrong_answer,
)


def run_game(game_name, game_description):
    """Runing the game.

    Args:
        game_name : game module from brain_games/games
        game_description : game description
    """
    user_name = welcome_dialog(game_description)
    for _ in range(3):
        (game_task, game_answer) = game_name()
        user_answer = qa_dialog(game_task)
        if user_answer != game_answer:
            wrong_answer(user_answer, game_answer, user_name)
            return
        correct()
    congratulations(user_name)
