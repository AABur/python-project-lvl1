"""Brain Games Engine."""

from brain_games.cli import qa_dialog, welcone_dialog, wrong_answer, сongratulations


def run_game(game_name, game_description):
    user_name = welcone_dialog(game_description)
    for _ in range(3):
        game_result = game_name()
        game_task = game_result[0]
        game_answer = game_result[1]
        user_answer = qa_dialog(game_task)
        if user_answer != game_answer:
            wrong_answer(user_answer, game_answer, user_name)
            return
        else:
            print("Correct!")
    сongratulations(user_name)
