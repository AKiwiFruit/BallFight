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

        # Character selections
        self.char1 = None
        self.char2 = None

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
                    ballsList = [ballFighters.SwordFighter, ballFighters.DaggerFighter, ballFighters.Brawler]
                    imageList = ["assets/Sword.png", "assets/Dagger.png", "assets/Brawler.png"]
                    # First Ball selections
                    for i in range(3):
                        if 50+75*i <= mouse_pos.x <= 100+75*i and self.screenDim.y-250 <= mouse_pos.y <= self.screenDim.y-200:
                            self.image1 = pygame.image.load(imageList[i]).convert_alpha()
                            self.image1 = pygame.transform.scale(self.image1, (self.screenDim.x-550, self.screenDim.y-400))
                            self.char1 = ballsList[i](Vector2(350,300))

                    # Second Ball selections
                    for i in range(3):
                        if self.screenDim.x-350+75*i <= mouse_pos.x <= self.screenDim.x-300+75*i and self.screenDim.y-250 <= mouse_pos.y <= self.screenDim.y-200:
                            self.image2 = pygame.image.load(imageList[i]).convert_alpha()
                            self.image2 = pygame.transform.scale(self.image2, (self.screenDim.x-550, self.screenDim.y-400))
                            self.char2 = ballsList[i](Vector2(450,300))
                    # Add more selections as needed

                    # Start Button clicked
                    if (self.screenDim.x/2-75 <= mouse_pos.x <= self.screenDim.x/2+75 and
                          self.screenDim.y-100 <= mouse_pos.y <= self.screenDim.y-50):
                        
                        character1, character2 = creation.getCharacters()

                        print(character1, character2)
                        if character1 is not None and character2 is not None:
                            game = ballSimGame.BallGame(character1, character2)
                            game.run()
                            self.Playing = False
                        

    def update(self):
        '''
        Update state
        '''
        pass

    def render(self):
        '''
        Render creation menu visuals
        '''
        self.screen.fill((42, 40, 40))  # dark grey background

        # Draw Preview Boxes
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 50, self.screenDim.x-500, self.screenDim.y-350), 5)
        display1 = pygame.draw.rect(self.screen, (255, 255, 255), (55, 55, self.screenDim.x-510, self.screenDim.y-360), 0)
        self.screen.blit(self.image1, display1)

        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-350, 50, self.screenDim.x-500, self.screenDim.y-350), 5)
        display2 = pygame.draw.rect(self.screen, (255, 255, 255), (self.screenDim.x-345, 55, self.screenDim.x-510, self.screenDim.y-360), 0)
        self.screen.blit(self.image2, display2)

        # Draw Selection Buttons
        colours = [(145, 35, 65), (85, 135, 65), (86, 86, 73)]
        labels = ["Sword", "Dagger", "Brawler"]

        # Draw buttons
        ## Use mod if need to add enough types to need new line
        for i in range(3):
            # First Ball boxes/buttons
            pygame.draw.rect(self.screen, (0, 0, 0), (50 + 75*i, self.screenDim.y-250, 50, 50), 5)
            pygame.draw.rect(self.screen, colours[i], (55 + 75*i, self.screenDim.y-245, 40, 40), 0)

            # Second Ball boxes/buttons
            pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x-350 + 75*i, self.screenDim.y-250, 50, 50), 5)
            pygame.draw.rect(self.screen, colours[i], (self.screenDim.x-345 + 75*i, self.screenDim.y-245, 40, 40), 0)
        
        # Draw labels
        for i in range(3):
            font = pygame.font.SysFont(None, 24)
            text = font.render(labels[i], True, (255, 255, 255))
            # First Ball Labels
            text_rect1 = text.get_rect(center=(75 + i*75, self.screenDim.y-175))
            self.screen.blit(text, text_rect1)
            # Second Ball Labels
            text_rect2 = text.get_rect(center=(self.screenDim.x-325 + i*75, self.screenDim.y-175))
            self.screen.blit(text, text_rect2)


        # Start Button
        if self.char1 is not None and self.char2 is not None:
            pygame.draw.rect(self.screen, (0, 200, 0), (self.screenDim.x/2-75, self.screenDim.y-100, 150, 50), 0)
            pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x/2-75, self.screenDim.y-100, 150, 50), 5)
            font = pygame.font.SysFont(None, 36)
            text = font.render("START", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screenDim.x/2, self.screenDim.y-75))
            self.screen.blit(text, text_rect)


        # Update display
        pygame.display.update()

    def getCharacters(self):
        '''
        Return the selected character classes
        '''
        return self.char1, self.char2

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
