# this file will contain the class "GameObject" which defines any object
# being used in the game
# it will store - 
# 1. position - point in centre of object - need vector
# 2. sprite - image to rep the object - can be loaded from utils.load_image()
# 3 radius - represents collision zone around object - integer indicating number of pixels from centre to edge of zone
# 4. velocity - movement value - need vector

# vectors are like tuples - can point to position but also rep motion or acceleration

from pygame.math import Vector2

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

    def move(self):
        self.position = self.position + self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius