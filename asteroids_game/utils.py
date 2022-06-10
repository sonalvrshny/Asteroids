# assets are resources used in games
# sprites are images used

from pygame.image import load

def load_image(name, with_alpha=True):
    path = f"assets/sprites/{name}.jpg"
    # load method returns a surface -used by Pygame to represent images
    loaded_image = load(path)

    # convert image to format that better fits the screen 
    # alpha used depending on transparent
    if with_alpha:
        return loaded_image.convert_alpha()
    else:
        return loaded_image.convert()