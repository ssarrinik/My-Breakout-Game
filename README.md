# 🧱 Python Turtle Breakout

A classic, retro-style Breakout clone built entirely in Python. This project uses the built-in `turtle` module for rendering graphics and physics, alongside `pygame` for handling immersive sound effects. 

The codebase is built with an Object-Oriented Game Manager pattern, ensuring clean, modular, and scalable logic.

---

## ✨ Features

* **Custom Physics Engine:** Precise ball-to-paddle and ball-to-brick collision detection.
* **Modular Architecture:** Entities (`Ball`, `Paddle`, `Brick`) are separated into distinct files for clean code management.
* **Dynamic Gameplay:** The ball reacts differently depending on where it strikes the paddle.
* **Audio Integration:** Uses `pygame.mixer` for cinematic hits, paddle bounces, and game-over sound effects.
* **Retro Visuals:** Clean, vibrant colors on a dark background using Turtle graphics.

---

## 📁 Project Structure

```text
├── entities/
│   ├── ball.py       # Handles ball drawing, movement, and position tracking
│   ├── paddle.py     # Handles paddle drawing and left/right movement
│   ├── brick.py      # Handles drawing, positioning, and deleting individual bricks
├── settings.py       # Global constants (screen limits, colors, brick counts)
├── game.py           # Core BreakoutGame class (game loop, collision logic, input handling)
├── main.py           # The entry point to launch the game
├── assets/           # (Optional) Folder to store your .mp3 sound files
└── README.md