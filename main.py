
import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Grid")

# Grid dimensions (you can modify these)
grid_length = 3  # l - number of rows
grid_width = 4   # w - number of columns

# Load the image
image = pygame.image.load('Untitled design (7).png')
# Scale image to fit grid nicely
scaled_width = screen.get_width() // grid_width
scaled_height = screen.get_height() // grid_length
image = pygame.transform.scale(image, (scaled_width, scaled_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill((0, 120, 120))
    
    # Draw grid of images
    for row in range(grid_length):
        for col in range(grid_width):
            x = col * scaled_width
            y = row * scaled_height
            screen.blit(image, (x, y))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
