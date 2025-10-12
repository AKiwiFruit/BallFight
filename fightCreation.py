import pygame
import random
from pygame.math import Vector2


class CreateSettings():
    def __init__(self):
        ''' 
        Initialize the settings creation window/instance 
        800x600 default size
        '''
        pygame.init()
        self.screenDim = Vector2(800, 600)
        self.screen = pygame.display.set_mode((self.screenDim.x, self.screenDim.y))
        pygame.display.set_caption("Ball Fight Simulator (Creation Mode)")
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
                self.screenDim = Vector2(event.w, event.h)
                self.screen = pygame.display.set_mode((self.screenDim.x, self.screenDim.y), pygame.RESIZABLE)

    def update(self):
        '''
        Update state
        '''
        pass

    def render(self):
        '''
        Render creation menu visuals
        '''
        self.screen.fill((41, 189, 193))  # Tealish background

        # Draw Preview Boxes
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 50, self.screenDim.x-500, self.screenDim.y-350), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (55, 55, self.screenDim.x-510, self.screenDim.y-360), 0)

        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-350, 50, self.screenDim.x-500, self.screenDim.y-350), 5)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screenDim.x-345, 55, self.screenDim.x-510, self.screenDim.y-360), 0)

        # Draw Settings Selection Boxes
        #TODO

        # Update display
        pygame.display.update()


    def run(self):
        '''
        Main loop
        '''
        while self.Playing:
            self.processEvents()
            self.update()
            self.render()
            # Cap the frame rate
            self.clock.tick(60)

creation = CreateSettings()
creation.run()
