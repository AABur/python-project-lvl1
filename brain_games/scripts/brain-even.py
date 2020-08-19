#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user
from brain_games.cli import answer
from brain_games.even import even


def main():
    print('Welcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    i = 1
    while i < 4:
        num = random.randint(1, 100)
        print('Question: {}'.format(num))
        ans = answer()
        if (even(num) and ans == 'yes') or (not even(num) and ans == 'no'):
            print('Correct!')
        elif ans == 'yes':
            return(print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again, {}!'.format(name)))
        elif ans == 'no':
            return(print('"no" is wrong answer ;(. Correct answer was "yes".\nLet\'s try again, {}!'.format(name)))
        else:
            return(print('Wrong answer ;(. \nLet\'s try again,{}!'.format(name)))
        i += 1
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
