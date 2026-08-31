# Poker vs AI

A Python/Pygame poker-style game where the player competes against a rules-based AI opponent. The AI uses starting-hand evaluation, pot odds, estimated card odds and hand-strength checks to decide whether to call, raise or fold.

## Features

- Playable game loop with player and AI turns
- Pygame interface with call, raise and fold actions
- Shuffled 52-card deck, community cards and betting rounds
- Pre-flop decisions based on a starting-hand lookup
- Post-flop decisions based on pot odds, estimated card odds and hand strength
- Hand evaluation from high card through to royal flush

## Requirements

- Python 3
- Pygame

## How to run

Install the dependency:

```bash
pip install -r requirements.txt
```

Start the game:

```bash
python game_screen.py
```

## Project structure

The code is split into modules for the Pygame interface, AI decision logic, card and deck handling, formatting and game data. It has been refactored to improve maintainability and readability while preserving the original gameplay logic.
