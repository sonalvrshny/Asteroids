# assets are resources used in games
# sprites are images used

import random

from pygame.image import load
from pygame.mixer import Sound
from pygame import Color
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

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)

def print_text(surface, text, font, color):
    # render has 3 args - the text, antialiasing flag for smoothening edges and color
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)

# so objects wrap around the screen instead of exiting
def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def random_position(surface):
    return Vector2(random.randrange(surface.get_width()), random.randrange(surface.get_height()))

def random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)
