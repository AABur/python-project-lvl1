"""Command line interface."""

import prompt


def welcome_dialog(task_msg):
    """Welcome dialog.

    Args:
        task_msg (str): Game description

    Returns:
        (str): User Name
    """
    print("Welcome to the Brain Games!\n{}\n".format(task_msg))
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def qa_dialog(task):
    """Q&A dialog.

    Show the task and request user answer

    Args:
        task (str): task example

    Returns:
        (str): User answer
    """
    print("Question: {}".format(task))
    return prompt.string("Your answer: ")


def congratulations(user_name):
    """User congratilations.

    Args:
        user_name (str): User name
    """
    print("Congratulations, {}".format(user_name))


def wrong_answer(user_answer, correct_answer, user_name):
    """Wrong answer info fo user.

    Inform user about wrong answer
    Interupt the game

    Args:
        user_answer (str): User Answer
        correct_answer (str): Correct Answer
        user_name (str): User Name
    """
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
    print("Let's try again, {}".format(user_name))


def correct():
    """Just Correct."""
    print("Correct!")
