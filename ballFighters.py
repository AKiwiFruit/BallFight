import pygame
from pygame.math import Vector2

class BallFighter():
    def __init__(self, position, velocity, acceleration, image, spin, radius, color, name: str, health=100,
                 mass=1.0):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.acceleration = Vector2(acceleration)
        self.image = image
        self.spin = spin
        self.radius = radius
        self.color = color
        self.health = health
        self.name = name
        self.mass = mass

    def getName(self) -> str:
        return self.name

    def move(self):
        dt = 1  # Future placeholder delta time

        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def draw(self, screen):
        # Body as a circle
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
        # Image overlay
        img = pygame.image.load(self.image).convert_alpha()
        img = pygame.transform.scale(img, (self.radius*2*2.5, self.radius*2*2.5))
        img_rect = img.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(img, img_rect)
        
        # Health display
        font = pygame.font.SysFont(None, 36)
        img = font.render(str(self.health), True, (220, 195, 200))
        screen.blit(img, img.get_rect(center=(int(self.position.x), int(self.position.y))))

class SwordFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/SwordFighter.png", spin=5, radius=40, color=(205, 50, 50), name="Sword")

class DaggerFighter(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/DaggerFighter.png", spin=5, radius=40, color=(50, 205, 50), name="Dagger")

class Brawler(BallFighter):
    def __init__(self, position, velocity = Vector2(2,2), acceleration = Vector2(0,0)):
        super().__init__(position, velocity, acceleration, "assets/Brawler.png", spin=5, radius=40, color=(86, 86, 73), name="Brawler")

# Can make more types here as wanted