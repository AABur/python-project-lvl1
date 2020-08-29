#!/usr/bin/env python3
"""Calc game script."""

from brain_games.engine import run_game
from brain_games.games.calc import game_calc


def main():
    """Calc game script."""
    run_game(game_calc, "What is the result of the expression?")


if __name__ == "__main__":
    main()
