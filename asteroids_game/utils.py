# assets are resources used in games
# sprites are images used

import random

from pygame.image import load
from pygame.math import Vector2

def load_image(name, with_alpha=True):
    path = f"assets/sprites/{name}"
    # load method returns a surface -used by Pygame to represent images
    loaded_image = load(path)

    # convert image to format that better fits the screen 
    # alpha used depending on transparent
    if with_alpha:
        return loaded_image.convert_alpha()
    else:
        return loaded_image.convert()

# so objects wrap around the screen instead of exiting
def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def random_position(surface):
    return Vector2(random.randrange(surface.get_width()), random.randrange(surface.get_height()))