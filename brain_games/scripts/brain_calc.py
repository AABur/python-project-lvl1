#!/usr/bin/env python3
"""Calc game script."""

from brain_games.engine import run_game
from brain_games.games.calc import GAME_DESCRIPTION, game_calc


def main():
    """Calc game script."""
    run_game(game_calc, GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
