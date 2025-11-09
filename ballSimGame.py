import pygame
import random
from pygame.math import Vector2
import ballFighters
from ballFighters import BallFighter
import numpy as np

class BallGame():
    def __init__(self, char1, char2):
        ''' 
        Initialize the game 
        Resizable window, 800x600 default size
        '''
        pygame.init()
        self.screenDim = Vector2(800, 600)
        self.screen = pygame.display.set_mode((self.screenDim.x, self.screenDim.y), pygame.RESIZABLE)
        pygame.display.set_caption("Ball Fight Simulator")
        self.clock = pygame.time.Clock()
        self.Playing = True
        self.character1 = char1
        self.character2 = char2

    def processEvents(self):
        ''' 
         Process events
         - Quit - Resize -
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Playing = False
                break
            elif event.type == pygame.VIDEORESIZE:
                # If window is resized, update the screen dimensions
                self.screenDim = Vector2(event.w, event.h)
                self.screen = pygame.display.set_mode((self.screenDim.x, self.screenDim.y), pygame.RESIZABLE)

    def update(self):
        '''
        Update game state
        TODO: health and damage system, weapon movement and stuff
        '''
        dt = 1  # Time delta placeholder for future use

        # Forces and acceleration updates can be added here
        g = Vector2(0, 0.05)  # Gravity coefficient (positive y is downwards)
        Fg1 = g*self.character1.mass # Gravitational force on character 1
        Fg2 = g*self.character2.mass # Gravitational force on character 2

        # Drag force, using 1 for mass density and radius/100 as reference area/length (Fd = 1/2 * massden * vel^2 * refL)
        # Absolute value and negative sign for motion opposition
        cd = 0.4 # drag coefficient
        Fdx1 = -1/2*0.005*self.character1.velocity.x*abs(self.character1.velocity.x)*cd*self.character1.radius/100 # Drag force x on character 1
        Fdy1 = -1/2*0.005*self.character1.velocity.y*abs(self.character1.velocity.y)*cd*self.character1.radius/100 # Drag force y on character 1
        Fd1 = Vector2(Fdx1, Fdy1)  # Total drag force on character 1
        Fdx2 = -1/2*0.005*self.character2.velocity.x*abs(self.character2.velocity.x)*cd*self.character2.radius/100 # Drag force x on character 2
        Fdy2 = -1/2*0.005*self.character2.velocity.y*abs(self.character2.velocity.y)*cd*self.character2.radius/100 # Drag force y on character 2
        Fd2 = Vector2(Fdx2, Fdy2)  # Total drag force on character 2

        # Net Forces
        Fnet1 = Fg1 + Fd1
        Fnet2 = Fg2 + Fd2
        
        # Update accelerations
        self.character1.acceleration = (Fnet1 / self.character1.mass) * dt
        self.character2.acceleration = (Fnet2 / self.character2.mass) * dt

        # move balls
        self.character1.move()
        self.character2.move()

        # Collision with walls (generates energy/speed)
        for character in [self.character1, self.character2]:
            if character.position.x - character.radius <= 100 or character.position.x + character.radius >= self.screenDim.x - 100:
                if character.velocity.x < 5:
                    character.velocity.x *= -1.15
                else:
                    character.velocity.x *= -1
                character.position.x = max(character.position.x, 100 + character.radius)
                character.position.x = min(character.position.x, self.screenDim.x - 100 - character.radius)

            if character.position.y - character.radius <= 100 or character.position.y + character.radius >= self.screenDim.y - 150:
                if character.velocity.y < 5:
                    character.velocity.y *= -1.15
                else:
                    character.velocity.y *= -1
                character.position.y = max(character.position.y, 100 + character.radius)
                character.position.y = min(character.position.y, self.screenDim.y - 150 - character.radius)

        # Collision between balls
        dist = self.character1.position.distance_to(self.character2.position)
        
        if dist <= self.character1.radius + self.character2.radius:
            
            # declare variables for cleaner final equation 
            x1 = self.character1.position.x
            y1 = self.character1.position.y
            v1x = self.character1.velocity.x
            v1y = self.character1.velocity.y
            v1 = np.hypot(v1x, v1y) # scalar speed of ball 1
            m1 = self.character1.mass
            if v1 == 0:
                cos1, sin1 = 0
            else:
                cos1 = v1x/v1
                sin1 = v1y/v1

            x2 = self.character2.position.x
            y2 = self.character2.position.y
            v2x = self.character2.velocity.x
            v2y = self.character2.velocity.y
            v2 = np.hypot(v2x, v2y) # scalar speed of ball 2
            m2 = self.character2.mass
            if v2 == 0:
                cos2, sin2 = 0
            else:
                cos2 = v2x/v2
                sin2 = v2y/v2

            # angle stuff
            # sin(theta-phi) = sin(theta)cos(phi) - cos(theta)sin(phi)
            # cos(theta-phi) = cos(theta)cos(phi) + sin(theta)sin(phi)
            phi = np.atan2(y2-y1, x2-x1) # contact angle
            cosphi = np.cos(phi)
            sinphi = np.sin(phi)
            cosphishift = np.cos(phi + np.pi/2)
            sinphishift = np.sin(phi + np.pi/2)

            cost1mp = cos1*cosphi + sin1*sinphi # cos(theta1 - phi)
            sint1mp = sin1*cosphi - cos1*sinphi # sin(theta1 - phi)

            cost2mp = cos2*cosphi + sin2*sinphi # cos(theta2 - phi)
            sint2mp = sin2*cosphi - cos2*sinphi # sin(theta2 - phi)

            # correct any overlapping
            overlap = 0.5 * (self.character1.radius + self.character2.radius - dist + 1e-6) # overlap error bound
            fracx = (x2 - x1) / dist # fraction of how much possible overlap would be x (negative if x1 bigger than x2)
            fracy = (y2 - y1) / dist # fraction of how much possible overlap would be y (negative if y1 bigger than y2)

            # move balls away slightly
            self.character1.position.x -= overlap * fracx
            self.character1.position.y -= overlap * fracy
            self.character2.position.x += overlap * fracx
            self.character2.position.y += overlap * fracy

            # Coefficient of restitution, 0 = perfectly inelastic, 1 = perfectly elastic, >1 = superelastic
            e = 1.1
            
            # Collision formula (started to derive then decided too much work when not perfectly elastic or inelastic
            # so i got the formula from wikipedia).
            self.character1.velocity.x = cosphi*(v1*cost1mp*(m1-m2) + (1+e)*m2*v2*cost2mp)/(m1 + m2) + v1*sint1mp*cosphishift
            self.character1.velocity.y = sinphi*(v1*cost1mp*(m1-m2) + (1+e)*m2*v2*cost2mp)/(m1 + m2) + v1*sint1mp*sinphishift

            self.character2.velocity.x = cosphi*(v2*cost2mp*(m2-m1) + (1+e)*m1*v1*cost1mp)/(m1 + m2) + v2*sint2mp*cosphishift
            self.character2.velocity.y = sinphi*(v2*cost2mp*(m2-m1) + (1+e)*m1*v1*cost1mp)/(m1 + m2) + v2*sint2mp*sinphishift
            


    def render(self):
        '''
        Render game visuals
        '''
        self.screen.fill((145, 63, 146))  # Clear screen with purple background

        # Draw Arena
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 100, self.screenDim.x-200, self.screenDim.y-250), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (105, 105, self.screenDim.x-210, self.screenDim.y-260), 0)

        # Draw Match Title
        font = pygame.font.SysFont(None, 64)
        title1 = font.render(self.character1.getName(), True, self.character1.color)
        vstitle = font.render( " VS ", True, (0, 0, 0))
        title2 = font.render(self.character2.getName(), True, self.character2.color)
        self.screen.blit(title1, title1.get_rect(center=(self.screenDim.x/4, 50)))
        self.screen.blit(vstitle, vstitle.get_rect(center=(self.screenDim.x/2, 50)))
        self.screen.blit(title2, title2.get_rect(center=(3*self.screenDim.x/4, 50)))

        # Draw Balls
        self.character1.draw(self.screen)
        self.character2.draw(self.screen)

        # Update display
        pygame.display.update()


    def run(self):
        '''
        Main game loop
        '''
        while self.Playing:
            self.processEvents()
            self.update()
            self.render()
            # Cap the frame rate
            self.clock.tick(60)
