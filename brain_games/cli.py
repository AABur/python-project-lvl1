import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print()
    return name


def answer():
    ans = prompt.string("Your answer: ")
    return ans
