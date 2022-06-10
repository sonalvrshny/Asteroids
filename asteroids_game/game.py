import pygame

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
        # creates display surface
        # surfaces can be drawn on one another
        # have to pass size of screen in display.set_mode
        self.screen = pygame.display.set_mode((800, 600))

    
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
        pass

    def draw(self):
        self.screen.fill((0, 0, 255))
        # updates the content of the screen 
        # this method will be called every frame to update display
        pygame.display.flip()