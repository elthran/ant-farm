import pygame


class KeyboardConstants:
    UP = "up"
    DOWN = "down"
    LEFT = "left"


class KeyboardUserMapping:
    """Maps the keys the user's keyboard presses to the keys in the PyGame engine"""

    def __init__(self):
        self.up = KeyboardConstants.UP
        self.down = KeyboardConstants.DOWN
        self.left = KeyboardConstants.LEFT
        self.event_mapper = KeyboardEventMapping(self)

    def key_cleaner(self, key):
        if key == pygame.K_UP:
            return self.up
        elif key == pygame.K_DOWN:
            return self.down
        elif key == pygame.K_LEFT:
            return self.left
        else:
            return "unknown"

    def key_change(self, key, change):
        key = self.key_cleaner(key)
        if change == "pressed":
            print(f"{key} was pressed.")
            self.event_mapper.mapper[key]()
        else:
            print(f"{key} was released.")


class KeyboardEventMapping:
    """Maps the keys in the PyGame engine to events in the game"""

    def __init__(self, keyboard_user_mapping):
        self.keyboard_user_mapping = keyboard_user_mapping
        self.mapper = {"up": self.do_nothing,
                       "down": self.do_nothing,
                       "left": self.swap_up_and_down_keys,
                       "unknown": self.do_nothing
        }

    def do_nothing(self):
        pass

    def swap_up_and_down_keys(self):
        print("Up and Down keys have swapped their mappings.")
        self.keyboard_user_mapping.up, \
        self.keyboard_user_mapping.down = self.keyboard_user_mapping.down, \
                                          self.keyboard_user_mapping.up
