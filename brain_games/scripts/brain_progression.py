#!/usr/bin/env python3
"""Progression game script."""


from brain_games.engine import run_game
from brain_games.games.progression import GAME_DESCRIPTION, run_progression


def main():
    """Progression game script."""
    run_game(run_progression, GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
