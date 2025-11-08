import pygame
import random
from pygame.math import Vector2
import ballFighters
from ballFighters import BallFighter

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
        TODO: Inelastic ball collision which adds energy into system, health and damage system, other impulses to get movement more active instead
        of just bouncing up and down.
        '''
        dt = 1  # Time delta placeholder for future use

        # Forces and acceleration updates can be added here
        g = Vector2(0, 0.1)  # Gravity coefficient (positive y is downwards)
        Fg1 = g*self.character1.mass # Gravitational force on character 1
        Fg2 = g*self.character2.mass # Gravitational force on character 2

        # Drag force, using 1 for mass density and radius/100 as reference area/length (Fd = 1/2 * massden * vel^2 * refL)
        # Absolute value and negative sign for motion opposition
        cd = 0.4 # drag coefficient
        Fdx1 = -1/2*0.001*self.character1.velocity.x*abs(self.character1.velocity.x)*cd*self.character1.radius/100 # Drag force x on character 1
        Fdy1 = -1/2*0.001*self.character1.velocity.y*abs(self.character1.velocity.y)*cd*self.character1.radius/100 # Drag force y on character 1
        Fd1 = Vector2(Fdx1, Fdy1)  # Total drag force on character 1
        Fdx2 = -1/2*0.001*self.character2.velocity.x*abs(self.character2.velocity.x)*cd*self.character2.radius/100 # Drag force x on character 2
        Fdy2 = -1/2*0.001*self.character2.velocity.y*abs(self.character2.velocity.y)*cd*self.character2.radius/100 # Drag force y on character 2
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

        # Collision with walls
        for character in [self.character1, self.character2]:
            if character.position.x - character.radius <= 100 or character.position.x + character.radius >= self.screenDim.x - 100:
                character.velocity.x *= -1.01
                character.position.x = max(character.position.x, 100 + character.radius)
                character.position.x = min(character.position.x, self.screenDim.x - 100 - character.radius)

            if character.position.y - character.radius <= 100 or character.position.y + character.radius >= self.screenDim.y - 150:
                character.velocity.y *= -1.01
                character.position.y = max(character.position.y, 100 + character.radius)
                character.position.y = min(character.position.y, self.screenDim.y - 150 - character.radius)

        # Collision between balls
        dist = self.character1.position.distance_to(self.character2.position)
        if dist <= self.character1.radius + self.character2.radius:
            # Simple collision response
            self.character1.velocity, self.character2.velocity = self.character2.velocity, self.character1.velocity

    def render(self):
        '''
        Render game visuals
        '''
        self.screen.fill((145, 63, 146))  # Clear screen with purple background

        # Draw Arena
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 100, self.screenDim.x-200, self.screenDim.y-250), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (105, 105, self.screenDim.x-210, self.screenDim.y-260), 0)

        # Draw Match Title
        font = pygame.font.SysFont(None, 48)
        title = font.render(self.character1.getName() + " VS " + self.character2.getName(), True, (0, 0, 0))
        self.screen.blit(title, title.get_rect(center=(self.screenDim.x/2, 50)))

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
