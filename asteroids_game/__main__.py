# creates new instance of game 
# start game by running main_loop()

from game import Asteroids

if __name__ == "__main__":
    asteroids = Asteroids()
    asteroids.main_loop()