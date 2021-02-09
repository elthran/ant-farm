from models.game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        game.handle_events()  # Check for key presses and handle logic per frame
        game.update()  # Move the sprites to new locations
        game.draw()  # Update the screen

