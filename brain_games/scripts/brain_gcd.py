#!/usr/bin/env python3
"""GCD game script."""

from brain_games.engine import run_game
from brain_games.games.gcd import game_gcd


def main():
    """GCD game script."""
    run_game(game_gcd, "Find the greatest common divisor of given numbers.")


if __name__ == "__main__":
    main()
