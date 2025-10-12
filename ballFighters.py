import pygame
from pygame.math import Vector2

class BallFighter():
    def __init__(self, position, velocity, color, radius):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.color = color
        self.radius = radius

    def move(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
