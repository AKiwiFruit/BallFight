import pygame
from pygame.math import Vector2
import numpy
import random
import ballWeapons

# This is so that every ball gets a new random, two swords shouldnt always get the same impulse
def randomizer(lower, upper):
    return random.randint(lower, upper)

class BallFighter():
    '''
    Superclass for the fighters who happen to be balls that bounce off walls
    '''
    def __init__(self, position, acceleration, image, radius, color, name: str, mass, weapon = None, health=100,
                 speedCap = 7):
        self.position = Vector2(position)
        self.velocity = Vector2(randomizer(-5, 5), randomizer(-5, 5))
        self.acceleration = Vector2(acceleration)
        self.image = image
        self.radius = radius
        self.color = color
        self.health = health
        self.name = name
        self.mass = mass
        self.weapon = weapon
        self.speedCap = speedCap

    def getName(self) -> str:
        '''
        I know this isn't needed, name isnt private, dont worry about it
        '''
        return self.name

    def move(self):
        dt = 1  # Future placeholder delta time if wanted
        
        # Update velocity and position (classical newtonian)
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        if self.weapon != None:
            self.weapon.update(self.position)

    def takeDamage(self, damage):
        '''
        takes damage from other ball, attacker is what has the damage attriubte, typically the weapon unles brawler
        '''
        self.health -= damage
        
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
        img = font.render(str(int(numpy.ceil(self.health))), True, (220, 195, 200))
        screen.blit(img, img.get_rect(center=(int(self.position.x), int(self.position.y))))


class SwordFighter(BallFighter):
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/SwordFighter.png", radius=40, color=(205, 50, 50), 
                         name="Sword", mass=1, weapon = ballWeapons.Sword(position))

class DaggerFighter(BallFighter):
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/DaggerFighter.png", radius=40, color=(50, 205, 50), 
                         name="Dagger", mass=1, weapon = ballWeapons.Dagger(position))

class Brawler(BallFighter):
    def __init__(self, position, acceleration = Vector2(0,0)):
        super().__init__(position, acceleration, "assets/Brawler.png", radius=40, color=(86, 86, 73), 
                         name="Brawler", mass=1.5, speedCap=10)

# Can make more types here as wanted