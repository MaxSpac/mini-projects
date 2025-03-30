# Goalie-Game
A simple yet addictive goalkeeper game built with Python and Pygame. You’re the keeper, using your mouse to block the ball before it hits the goal. Choose your keeper’s name, rack up your score, and avoid the dreaded "Game Over" as long as possible!


## Features
- Keeper Name Selection: Pick from "Manuel N.", "Rainer W.", or enter a custom name (max 8 characters).
- Dynamic Difficulty: Ball speed increases with every successful block.
- Realistic Physics: If unblocked, the ball flies into the goal and stays at the bottom until a new game starts.
- Game Over Animation: A dramatic rotating "Game Over!" text followed by a "You Loser!" message.
- Restart or Quit: Press "R" to restart or "Q" to quit after Game Over.


## Installation

#### Requirements:
- Python 3.x (tested with 3.9+)
- Pygame library (pip install pygame)

#### Steps:
- Clone or download this repository.
- Navigate to the directory with cd goalie-game (or your folder name).
- Run the game with:
    bash
    python goalie_game.py

## Controls
Before the Game:
- Click "Manuel N." or "Rainer W." for a predefined name.
- Click the input field, type a custom name (max 8 characters), and press Enter.

In-Game:
- Move the mouse horizontally to control the keeper.
- Block the ball before it crosses the goal line.

Game Over:
- Press "R" to restart.
- Press "Q" to quit.

Gameplay
- Objective: Block as many balls as possible to increase your score.
- Ball: Starts at the top with a speed of 5 pixels/frame, increasing by 0.25 per block.
- Collision: The keeper’s collision zone dynamically adjusts to the ball speed (ball_speed // 5) to prevent skipping.
- Game Over: Triggered when the ball crosses the goal line (y=500). The ball then falls to the bottom of the goal (y=550) and stays there.


## Technical Details
- Window Size: 800x600 pixels
- Framerate: 60 FPS

Colors:
- Ball: Red
- Keeper: Green (name in black inside the rect)
- Goal: White
- Background: Black

Limits:
- Reliable up to approximately 108 blocks (at ball_speed = 32), thanks to the dynamic collision zone.
- Known Limitations: At extremely high speeds (beyond 108 blocks), the ball might skip the collision zone, though this exceeds typical human performance. Input is limited to 8 characters   (adjustable in the code).

## Improvement Ideas:
- Add a high-score system.
- Include sound effects for blocks and Game Over.
- Offer more keeper options or customizable colors.

## Developer:
Developed by Max Schwarzkopf with assistance from Grok (xAI). Questions or suggestions? Let me know!
