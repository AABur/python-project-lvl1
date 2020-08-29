#!/usr/bin/env python3
"""Even game script."""

from brain_games.engine import run_game
from brain_games.games.even import game_even


def main():
    """Even game script."""
    run_game(
        game_even,
        'Answer \033[31m"yes"\033[m if number even otherwise answer \033[31m"no"\033[m',
    )


if __name__ == "__main__":
    main()
