# Poker vs AI

A Python/Pygame poker game where the player competes against a simple AI opponent. The AI uses starting-hand evaluation, pot odds, card odds, and hand-strength checks to decide whether to call, raise, or fold.

## Features

- Playable poker-style game loop with player and AI turns
- Pygame interface with call, raise, and fold actions
- Deck generation, shuffling, dealing, and community cards
- AI betting decisions based on hand evaluation and odds
- Starting-hand lookup from `cardeval.txt`

## Tech Stack

- Python
- Pygame

## How to Run

Install Pygame:

```bash
pip install pygame
```

Run the game:

```bash
python gameScreen.py
```

## Project Status

This project is being refactored to improve maintainability, readability, and structure while preserving the original gameplay logic.
