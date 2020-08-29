#!/usr/bin/env python3
"""Prime game script."""

from brain_games.engine import run_game
from brain_games.games.prime import game_prime


def main():
    """Prime game script."""
    run_game(
        game_prime,
        'Answer \033[31m"yes"\033[m if number prime otherwise answer \033[31m"no"\033[m',
    )


if __name__ == "__main__":
    main()
