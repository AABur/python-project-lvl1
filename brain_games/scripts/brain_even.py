#!/usr/bin/env python3
"""Even game script."""

from brain_games.engine import run_game
from brain_games.games.even import GAME_DESCRIPTION, run_even


def main():
    """Even game script."""
    run_game(run_even, GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
