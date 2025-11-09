import pygame
from pygame.math import Vector2

def rotateAboutPivot(image, angle, pivot, origin):
    
    rotation = pygame.transform.rotate(image, angle)

    offset = pivot + (origin - pivot).rotate(-angle)

    rect = rotation.get_rect(center = offset)

    return rotation, rect

class Weapon():
    '''
    give pivot
    '''
    def __init__(self, pivot, image, spinSpeed, damage, length = 200, startAngle = 0):
        self.pivot = pivot
        self.angle = 0
        self.image = image
        self.originalImage = image
        self.spinSpeed = spinSpeed
        self.damage = damage
        self.length = length

        offset = Vector2()
        offset.from_polar((self.length, -startAngle))

        self.position = pivot + offset
        
        self.rect = self.image.get_rect(center = self.position)

    
    def update(self):
        dt = 1
        self.angle += 1*dt

        self.image, self.rect = rotateAboutPivot(self.originalImage, self.angle, self.pivot, self.position)

    def draw(self, screen):

        pygame.draw.line(screen, 'black', self.pivot, self.rect.center)
        screen.blit(self.image, self.rect)

class Sword(Weapon):
    def __init__(self, pivot):
        swordImage = pygame.image.load("assets/SwordWeapon.png").convert_alpha()
        scaledSwordImage = pygame.transform.scale(swordImage, (150, 150))
        super().__init__(pivot, image = scaledSwordImage, spinSpeed = 5, damage = 1, length = 80, startAngle=45)