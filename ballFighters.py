import pygame
from pygame.math import Vector2
import random
import ballWeapons

def randomizer(lower, upper):
    return random.randint(lower, upper)

class BallFighter():
    def __init__(self, position, acceleration, image, spin, radius, color, name: str, mass, weapon = None, health=100):
        self.position = Vector2(position)
        self.velocity = Vector2(randomizer(-5, 5), randomizer(-5, 5))
        self.acceleration = Vector2(acceleration)
        self.image = image
        self.spin = spin
        self.radius = radius
        self.color = color
        self.health = health
        self.name = name
        self.mass = mass
        self.weapon = weapon

    def getName(self) -> str:
        return self.name

    def move(self):
        dt = 1  # Future placeholder delta time if wanted
        
        # Update velocity and position (classical newtonian)
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        if self.weapon != None:
            self.weapon.update(self.position)
        

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
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/SwordFighter.png", spin=5, radius=40, color=(205, 50, 50), 
                         name="Sword", mass=1, weapon = ballWeapons.Sword(position))

class DaggerFighter(BallFighter):
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/DaggerFighter.png", spin=5, radius=40, color=(50, 205, 50), 
                         name="Dagger", mass=1, weapon = ballWeapons.Dagger(position))

class Brawler(BallFighter):
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/Brawler.png", spin=5, radius=40, color=(86, 86, 73), name="Brawler", mass=2)

# Can make more types here as wanted