import pygame
import random
import math

# Initialize Pygame 
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

Playing = True
while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
            break
        elif event.type == pygame.VIDEORESIZE:
            # If window is resized, update the screen dimensions
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    screen.fill((145, 63, 146))  # Clear screen with purple background

    # Draw Arena
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, WIDTH-200, HEIGHT-250), 5)
    pygame.draw.rect(screen, (255, 255, 255), (105, 105, WIDTH-210, HEIGHT-260), 0)

    # Update display
    pygame.display.update()






# Final exit of application
pygame.quit()
