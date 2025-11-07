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
        '''
        dt = 1  # Time delta placeholder for future use

        # move balls
        self.character1.move()
        self.character2.move()

        # Forces and acceleration updates can be added here
        g = Vector2(0, 1)  # Gravity force vector
        self.character1.acceleration = g
        self.character2.acceleration = g

        # Collision with walls
        for character in [self.character1, self.character2]:
            if character.position.x - character.radius <= 100 or character.position.x + character.radius >= self.screenDim.x - 100:
                character.velocity.x *= -1
                character.position.x = max(character.position.x, 100 + character.radius)
                character.position.x = min(character.position.x, self.screenDim.x - 100 - character.radius)

            if character.position.y - character.radius <= 100 or character.position.y + character.radius >= self.screenDim.y - 150:
                character.velocity.y *= -1
                character.position.y = max(character.position.y, 100 + character.radius)
                character.position.y = min(character.position.y, self.screenDim.y - 150 - character.radius)



        # Collision between balls
        dist = self.character1.position.distance_to(self.character2.position)
        if dist <= self.character1.radius + self.character2.radius:
            # Simple elastic collision response
            self.character1.velocity, self.character2.velocity = self.character2.velocity, self.character1.velocity

        ## TODO: Add PHYSICS (acceleration, force)

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

#game = BallGame()
#game.run()
