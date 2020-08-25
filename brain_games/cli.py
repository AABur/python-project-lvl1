""" Библиотека пользовательского интерфейса """
import prompt


def welcome_user(task_msg):
    """ Приветствие пользователя """
    print("Welcome to the Brain Games!")
    print(task_msg + "\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def answer(question):
    print("Question: {}".format(question))
    return prompt.string("Your answer: ")
