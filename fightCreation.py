import pygame
import random
from pygame.math import Vector2
import ballFighters
import ballSimGame


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

        # Load default images for preview boxes
        self.image1 = pygame.image.load("assets/Blank.png").convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (self.screenDim.x-510, self.screenDim.y-360))

        self.image2 = pygame.image.load("assets/Blank.png").convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (self.screenDim.x-510, self.screenDim.y-360))

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = Vector2(event.pos)
                    # Check for selection boxes being clicked to select character
                    match mouse_pos:
                        case _ if 50 <= mouse_pos.x <= 100 and self.screenDim.x-450 <= mouse_pos.y <= self.screenDim.x-400:
                            # First Ball - Sword
                            self.image1 = pygame.image.load("assets/Sword.png").convert_alpha()
                            self.image1 = pygame.transform.scale(self.image1, (self.screenDim.x-550, self.screenDim.y-400))

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
        display1 = pygame.draw.rect(self.screen, (255, 255, 255), (55, 55, self.screenDim.x-510, self.screenDim.y-360), 0)
        self.screen.blit(self.image1, display1)

        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-350, 50, self.screenDim.x-500, self.screenDim.y-350), 5)
        display2 = pygame.draw.rect(self.screen, (255, 255, 255), (self.screenDim.x-345, 55, self.screenDim.x-510, self.screenDim.y-360), 0)
        self.screen.blit(self.image2, display2)

        # Draw Settings Selection Boxes
        ## First Ball
        ### Sword
        pygame.draw.rect(self.screen, (0, 0, 0), (50, self.screenDim.x-450, 50, 50), 5)
        pygame.draw.rect(self.screen, (145, 35, 65), (55, self.screenDim.x-445, 40, 40), 0)

        ### Dagger
        pygame.draw.rect(self.screen, (0, 0, 0), (125, self.screenDim.x-450, 50, 50), 5)
        pygame.draw.rect(self.screen, (85, 135, 65), (130, self.screenDim.x-445, 40, 40), 0)       

        ## Second Ball
        ### Sword
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-350, self.screenDim.x-450, 50, 50), 5)
        pygame.draw.rect(self.screen, (145, 35, 65), (self.screenDim.x-345, self.screenDim.x-445, 40, 40), 0)

        ### Dagger
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-275, self.screenDim.x-450, 50, 50), 5)
        pygame.draw.rect(self.screen, (85, 135, 65), (self.screenDim.x-270, self.screenDim.x-445, 40, 40), 0)

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
