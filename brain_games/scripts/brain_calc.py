#!/usr/bin/env python3
    """game script."""

from brain_games.cli import welcone_dialog, qa_dialog, сongratulations, wrong_answer
from brain_games.games.calc import game_calcqa_dialog, сongratulations, wrong_answer
from brain_games.games.calc import game_calc


def main():
    user_name = welcone_dialog("What is the result of the expression?")
    i = 1
    while i < 4:
        game = game_calc
        print(game)  # TODO - remove it
        task = game_calc[0]
        correct_answer = game_calc[1]
        user_answer = qa_dialog(task)
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
        i += 1
    сongratulations(user_name)


if __name__ == "__main__":
    main()
