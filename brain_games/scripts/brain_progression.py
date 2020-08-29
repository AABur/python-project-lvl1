#!/usr/bin/env python3
"""Progression game script."""


from brain_games.engine import run_game
from brain_games.games.progression import game_progression


def main():
    """Progression game script."""
    run_game(game_progression, "What number is missing in the progression?")


if __name__ == "__main__":
    main()
