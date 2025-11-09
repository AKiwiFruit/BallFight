import pygame
from pygame.math import Vector2

def rotateAboutPivot(image, angle, pivot, origin):
    '''
    Rotate image and rect about the pivot
    returns image, rect
    '''
    rotation = pygame.transform.rotate(image, angle)
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = rotation.get_rect(center = offset)

    return rotation, rect

class Weapon():
    '''
    Superclass of weapons for the fighters:
    pivot, image, spinSpeed, damage, length = 200, startAngle = 0
    '''
    def __init__(self, pivot, image, spinSpeed, damage, length = 100, startAngle = 0):
        self.pivot = pivot
        self.angle = 0
        self.image = image
        self.originalImage = image
        self.spinSpeed = spinSpeed
        self.damage = damage
        self.length = length
        self.startAngle = startAngle

        # Distance from pivot
        offset = Vector2()
        offset.from_polar((self.length, -startAngle))

        # actual position
        self.position = pivot + offset
        
        self.rect = self.image.get_rect(center = self.position)

    
    def update(self, newPiv: Vector2):
        '''
        update weapon stuff, needs new position of pivot
        '''
        dt = 1
        self.angle += self.spinSpeed*dt

        # update positions
        self.pivot = newPiv
        offset = Vector2()
        offset.from_polar((self.length, -self.startAngle + dt))
        self.position = self.pivot + offset

        # new rotated image and rect
        self.image, self.rect = rotateAboutPivot(self.originalImage, self.angle, self.pivot, self.position)

    def draw(self, screen):
        pygame.draw.line(screen, 'black', self.pivot, self.rect.center)
        screen.blit(self.image, self.rect)

class Sword(Weapon):
    '''
    Sword for the SwordFighter
    '''
    def __init__(self, pivot):
        swordImage = pygame.image.load("assets/SwordWeapon.png").convert_alpha()
        scaledSwordImage = pygame.transform.scale(swordImage, (200, 200))
        super().__init__(pivot, image = scaledSwordImage, spinSpeed = 2, damage = 1, length = 80, startAngle=45)

class Dagger(Weapon):
    '''
    Dagger for the DaggerFighter
    '''
    def __init__(self, pivot):
        daggerImage = pygame.image.load("assets/DaggerWeapon.png").convert_alpha()
        scaledDaggerImage = pygame.transform.scale(daggerImage, (175, 175))
        super().__init__(pivot, image = scaledDaggerImage, spinSpeed = 5, damage = 1, length = 60, startAngle=-45)