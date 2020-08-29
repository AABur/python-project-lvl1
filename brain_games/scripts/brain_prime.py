#!/usr/bin/env python3
"""Prime game script."""

from brain_games.engine import run_game
from brain_games.games.prime import GAME_DESCRIPTION, game_prime


def main():
    """Prime game script."""
    run_game(game_prime, GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
