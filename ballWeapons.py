import pygame
from pygame.math import Vector2

class Weapon():
    def __init__(self, position, image, spinSpeed, damage):
        self.position = position
        self.image = image
        self.spinSpeed = spinSpeed
        self.damage = damage

    
    def move(self):
        pass

    def draw(self, screen):
        pass