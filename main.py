from seeds import game

if __name__ == "__main__":
    game = game
    while True:
        game.handle_events()  # Check for key presses and handle logic per frame
        game.update()  # Move the sprites to new locations
        game.draw()  # Update the screen

