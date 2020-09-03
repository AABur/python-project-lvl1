#!/usr/bin/env python3
"""GCD game script."""

from brain_games.engine import run_game
from brain_games.games.gcd import GAME_DESCRIPTION, run_gcd


def main():
    """GCD game script."""
    run_game(run_gcd, GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
