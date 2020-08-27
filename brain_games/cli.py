""" Command line interface """
import prompt


def welcome_user(task_msg):  # TODO old version - delite
    """ Приветствие пользователя """
    print("Welcome to the Brain Games!")
    print(task_msg + "\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def answer(question):  # TODO old version - delite
    print("Question: {}".format(question))
    return prompt.string("Your answer: ")


def welcone_dialog(task_msg):
    """Welcome dialog

    Args:
        task_msg (str): Game description

    Returns:
        (str): User Name
    """
    print("Welcome to the Brain Games!")
    print(task_msg + "\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def qa_dialog(task):
    """Q&A dialoh

    Show the task and request user answer

    Returns:
        (str): User answer
    """
    print("Question: {}".format(task))
    return prompt.string("Your answer: ")


def сongratulations(user_name):
    """User congratilations

    Args:
        user_name (str): User name
    """
    print("сongratulations")


def wrong_answer(user_answer, correct_answer, user_name):
    """Wrong answer info fo user

Inform user about correct answer
Interupt the game

    Args:
        user_answer (str): User Answer
        correct_answer (str): Correct Answer
        user_name (str): User Answer
    """
    print("wrong")
