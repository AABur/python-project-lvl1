#!/usr/bin/env python3
"""Calc game script"""

from brain_games.cli import qa_dialog, welcone_dialog, wrong_answer, сongratulations
from brain_games.games.calc import game_calc


def main():
    user_name = welcone_dialog("What is the result of the expression?")
    for i in range(3):
        game = game_calc()
        task = game[0]
        correct_answer = game[1]
        user_answer = qa_dialog(task)
        if user_answer != correct_answer:
            wrong_answer(user_answer, correct_answer, user_name)
            return
        else:
            print("Correct!")
    сongratulations(user_name)


if __name__ == "__main__":
    main()
