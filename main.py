
import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Display")

# Load the image (replace 'image.png' with your image file)
image = pygame.image.load('image.png')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with white
    screen.fill((255, 255, 255))
    
    # Draw the image at position (0, 0)
    screen.blit(image, (0, 0))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
