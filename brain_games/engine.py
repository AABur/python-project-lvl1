"""Brain Games Engine."""

import prompt

GAME_STEPS = 3


def run_game(game_module):
    """Brain Games Engine.

    Executing game process

    Args:
        game_module (function): game engine module
    """
    say_welcome(game_module.GAME_DESCRIPTION)
    user_name = get_user_name()
    for step in range(GAME_STEPS):
        (game_task, game_answer) = game_module.game_engine()
        user_answer = get_user_answer(game_task)
        if user_answer != game_answer:
            notify_wrong_answer(user_answer, game_answer, user_name)
            return
        confirm_correct_answer()
    congratulate(user_name)


def get_user_name():
    """Get user name dialog.

    Returns:
        (str): User Name
    """
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def get_user_answer(task):
    """Q&A dialog.

    Show the task and request user answer

    Args:
        task (str): task example

    Returns:
        (str): User answer
    """
    return prompt.string("Question: {}\nYour answer: ".format(task))


def say_welcome(task_msg):
    """Say welcome and print game rules."""
    print("Welcome to the Brain Games!\n{}\n".format(task_msg))


def congratulate(user_name):
    """User congratilations.

    Args:
        user_name (str): User name
    """
    print("Congratulations, {}".format(user_name))


def notify_wrong_answer(user_answer, correct_answer, user_name):
    """Wrong answer info fo user.

    Inform user about wrong answer

    Args:
        user_answer (str): User Answer
        correct_answer (str): Correct Answer
        user_name (str): User Name
    """
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
        user_answer, correct_answer))
    print("Let's try again, {}!".format(user_name))


def confirm_correct_answer():
    """Just confirm correct answer."""
    print("Correct!")
