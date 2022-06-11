import pygame
from models import GameObject
from utils import load_image

# The general structure of a Pygame program looks like:
# initialize_pygame()
# while True:
#     handle_input()
#     process_game_logic()
#     draw_game_elements()

class Asteroids:
    def __init__(self):
        # initializes game
        self.init_pygame()
        # have to make sure game runs similarly on diff processors
        # asteroids and bullets should have same relative velocity
        # otherwise game may be easier or harder depending on processor
        # to ensure uniformity, use pygame.time.Clock - will wait to 
        # match FPS value
        self.clock = pygame.time.Clock()
        # creates display surface
        # surfaces can be drawn on one another
        # have to pass size of screen in display.set_mode
        self.screen = pygame.display.set_mode((1600, 1200))
        # set background image
        self.background = load_image("bg_image.jpg", False)
        self.spaceship = GameObject((800, 600), load_image("spaceship.png"), (0,0))
        self.asteroid = GameObject((800, 600), load_image("asteroid.png"), (1,0))

    
    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    # one-time initialization of Pygame
    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

    def handle_input(self):
        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    def draw(self):
        # to display one surface on top of another, use blit on surface to draw on
        # first arg is the surface to draw on, second is point to draw
        self.screen.blit(self.background, (0,0))

        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)

        # updates the content of the screen 
        # this method will be called every frame to update display
        pygame.display.flip()
        # will run at 60 fps
        self.clock.tick(60)