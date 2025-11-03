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
        # Body as a circle
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
        # Image overlay
        img = pygame.image.load(self.image).convert_alpha()
        img = pygame.transform.scale(img, (self.radius*2*2.5, self.radius*2*2.5))
        img_rect = img.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(img, img_rect)

class SwordFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/SwordFighter.png", spin=5, radius=40, color=(205, 50, 50))

class DaggerFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/DaggerFighter.png", spin=5, radius=40, color=(50, 205, 50))

class Brawler(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/Brawler.png", spin=5, radius=40, color=(86, 86, 73))

# Can make more types here as wanted