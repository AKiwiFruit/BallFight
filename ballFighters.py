import pygame
from pygame.math import Vector2

class BallFighter():
    def __init__(self, position, velocity, acceleration, image, spin, radius, color):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.acceleration = Vector2(acceleration)
        self.image = image
        self.spin = spin
        self.radius = radius
        self.color = color

    def move(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

class SwordFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/Sword.png", spin=5, radius=20, color=(205, 50, 50))

class DaggerFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/Dagger.png", spin=5, radius=20, color=(50, 205, 50))

class Brawler(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/Brawler.png", spin=5, radius=20, color=(86, 86, 73))

# Can make more types here as wanted