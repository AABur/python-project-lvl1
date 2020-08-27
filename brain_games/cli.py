""" Command line interface """
import prompt


def welcone_dialog(task_msg):
    """Welcome dialog

    Args:
        task_msg (str): Game description

    Returns:
        (str): User Name
    """
    print("\nWelcome to the Brain Games!")
    print(task_msg + "\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def qa_dialog(task):
    """Q&A dialog

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
    print("\033[31mCongratulations, \033[1m{}\033[0;31m!\033[m".format(user_name))


def wrong_answer(user_answer, correct_answer, user_name):
    """Wrong answer info fo user

    Inform user about correct answer
    Interupt the game

    Args:
        user_answer (str): User Answer
        correct_answer (str): Correct Answer
        user_name (str): User Answer
    """
    print(
        "\033[31m'{}'\033[m is wrong answer ;(. Correct answer was \033[31m'{}'\033[m.".format(
            user_answer, correct_answer
        )
    )
    print("Let's try again, \033[1m{}\033[m!".format(user_name))
