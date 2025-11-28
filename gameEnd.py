import pygame
from pygame import Vector2

class gameEnd():
    def __init__(self, winner):
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

        if (winner == None):
            self.image = "assets\Blank.png"
            self.name = "TIE"
        else:
            self.image = winner.image
            self.name = winner.name

        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.screenDim.x-510, self.screenDim.y-360))

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

                    # Start Button clicked
                    if (self.screenDim.x/2-75 <= mouse_pos.x <= self.screenDim.x/2+75 and
                        self.screenDim.y-100 <= mouse_pos.y <= self.screenDim.y-50):
                        import fightCreation
                        fightCreation.CreateSettings().run()
                        self.Playing = False

    def update(self):
        '''
        Update state
        '''
        pass

    def render(self):
        '''
        Render game end visuals
        '''
        self.screen.fill((42, 40, 40))  # dark grey background

        pygame.draw.rect(self.screen, (0, 0, 0), (200, 100, self.screenDim.x-400, self.screenDim.y-250), 5)
        displayWinner = pygame.draw.rect(self.screen, (255, 255, 255), (205, 105, self.screenDim.x-410, self.screenDim.y-260), 0)
        self.screen.blit(pygame.transform.scale(self.image, displayWinner.size), displayWinner)

        # New Game Button
        pygame.draw.rect(self.screen, (0, 200, 0), (self.screenDim.x/2-75, self.screenDim.y-100, 150, 50), 0)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screenDim.x/2-75, self.screenDim.y-100, 150, 50), 5)
        font = pygame.font.SysFont(None, 36)
        text = font.render("AGAIN?", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screenDim.x/2, self.screenDim.y-75))
        self.screen.blit(text, text_rect)

        # WINNER
        font = pygame.font.SysFont(None, 80)
        winnertitle = font.render( " WINNER ", True, (0, 0, 0))
        self.screen.blit(winnertitle, winnertitle.get_rect(center=(self.screenDim.x/2, 50)))

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



