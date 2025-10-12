import pygame
import random
import math


class BallGame():
    def __init__(self):
        ''' 
        Initialize the game 
        Resizable window, 800x600 default size
        '''
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Ball Fight Simulator")
        self.clock = pygame.time.Clock()
        self.Playing = True

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
                self.WIDTH, self.HEIGHT = event.w, event.h
                self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

    def update(self):
        '''
        Update game state
        '''
        pass

    def render(self):
        '''
        Render game visuals
        '''
        self.screen.fill((145, 63, 146))  # Clear screen with purple background

        # Draw Arena
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 100, self.WIDTH-200, self.HEIGHT-250), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (105, 105, self.WIDTH-210, self.HEIGHT-260), 0)

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

game = BallGame()
game.run()
