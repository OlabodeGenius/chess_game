# Chess Game

A simple chess game implemented in Python using Pygame and the `python-chess` library. This project allows you to play chess against a basic AI opponent or against another player. The game features a graphical user interface (GUI) that displays the chessboard and pieces.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Contributing](#contributing)
- [License](#license)

## Features

- Play against a simple AI opponent.
- Two-player mode (player vs. player).
- Graphical user interface with a chessboard and pieces.
- Basic move validation and piece movement.
- Piece images that can be easily replaced.

## Installation

To run this project, you need to have Python and Pygame installed on your machine. Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/chess_game.git
   cd chess_game
Create a virtual environment (optional but recommended):
bash

Copy Code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
bash

Copy Code
pip install pygame python-chess
Add chess piece images:
Create a directory named images in the project root.
Add the following images to the images directory:
white_pawn.png
white_knight.png
white_bishop.png
white_rook.png
white_queen.png
white_king.png
black_pawn.png
black_knight.png
black_bishop.png
black_rook.png
black_queen.png
black_king.png
Ensure the images are sized appropriately (e.g., 100x100 pixels).

Usage
To start the game, run the following command:

python gui.py

This will launch the chess game window where you can start playing.

Gameplay
Selecting a Piece: Click on a white piece to select it.
Moving a Piece: After selecting a piece, click on a valid destination square to move it.
AI Opponent: After the player makes a move, the AI will automatically make its move.
Game Over: The game will continue until you close the window.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
