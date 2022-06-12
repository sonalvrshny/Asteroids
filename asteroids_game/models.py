# this file will contain the class "GameObject" which defines any object
# being used in the game
# it will store - 
# 1. position - point in centre of object - need vector
# 2. sprite - image to rep the object - can be loaded from utils.load_image()
# 3 radius - represents collision zone around object - integer indicating number of pixels from centre to edge of zone
# 4. velocity - movement value - need vector

# vectors are like tuples - can point to position but also rep motion or acceleration

from pygame import Surface
from pygame.math import Vector2
from pygame.transform import rotozoom


from utils import load_image, wrap_position


# ref variables
UP = Vector2(0,-1)


# represents all the objects which are used in the game
class GameObject:
    def __init__(self, position, sprite, velocity):
        # casting done to Vector2 to convert arguments passed as tuples
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width()/2
        self.velocity = Vector2(velocity)

    # draw the object's sprite on the surface passed
    def draw(self, surface):
        # calculate correct position for blitting image
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position((self.position + self.velocity), surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

class Spaceship(GameObject):
    # determines how fast spaceship can rotate
    MANEUVERABILITY = 3
    ACCELERATION = 0.25

    def __init__(self, position):
        # make copy of original vector UP
        self.direction = Vector2(UP)
        super().__init__(position, load_image("spaceship.png"), Vector2(0))

    def rotate(self, clockwise = True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign 
        # rotate_ip rotates in place by a given angle in degrees
        self.direction.rotate_ip(angle)

    # override draw method
    def draw(self, surface):
        # calculate the angle by which one vector needs to be rotated
        angle = self.direction.angle_to(UP)
        # rotates the sprite, 1.0 is scale that should be applied (don't want to scale)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        # recalculate blit position
        rotated_surface_size = Vector2(rotated_surface.get_size())
        # multiplying by 0.5 returns a vector half the length of original
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def decelerate(self):
        self.velocity -= self.direction * self.ACCELERATION
