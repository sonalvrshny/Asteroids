import pygame
from models import GameObject
from utils import load_image, random_position, print_text, load_sound
from models import Spaceship, Asteroid

# The general structure of a Pygame program looks like:
# initialize_pygame()
# while True:
#     handle_input()
#     process_game_logic()
#     draw_game_elements()

LOST = "You lost!"
WON = "You won!"

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
        self.destroy_sound = load_sound("destroy")
        # set text font and message
        self.font = pygame.font.Font(None, 128)
        self.message = ""

        self.bullets = []
        self.asteroids = []
        self.spaceship = Spaceship((800,600), self.bullets.append)
        # include 6 asteroids at random positions
        # have to make sure that any asteroid does not start in region of spaceship
        for _ in range(1):
            while True:
                position = random_position(self.screen)
                if (position.distance_to(self.spaceship.position)) > 250:
                    break
            self.asteroids.append(Asteroid(position, self.asteroids.append))
        

    # helper method that can be used to return all objects being used in game
    def get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        # have to make sure destroyed spaceship is not added
        if self.spaceship:
            game_objects.append(self.spaceship)
        return game_objects
    
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
            elif (self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                self.spaceship.shoot()


        # if spaceship is not destroyed
        if self.spaceship:
            # change direction of spaceship
            is_key_pressed = pygame.key.get_pressed()
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)

            # ac/decelerate the spaceship
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()
            elif is_key_pressed[pygame.K_DOWN]:
                self.spaceship.decelerate()

    def process_game_logic(self):
        for object in self.get_game_objects():
            object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.message = LOST
                    break
        
        # collide with asteroids
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    self.destroy_sound.play()
                    break

        # remove bullets if they leave the screen to improve performance
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = WON



    def draw(self):
        # to display one surface on top of another, use blit on surface to draw on
        # first arg is the surface to draw on, second is point to draw
        self.screen.blit(self.background, (0,0))

        for object in self.get_game_objects():
            object.draw(self.screen)

        # if the game is over, message should be displayed based on result
        if self.message:
            if self.message == WON:
                print_text(self.screen, self.message, self.font, pygame.Color("darkgreen"))
            elif self.message == LOST:
                print_text(self.screen, self.message, self.font, pygame.Color("tomato"))            

        # updates the content of the screen 
        # this method will be called every frame to update display
        pygame.display.flip()
        # will run at 60 fps
        self.clock.tick(60)