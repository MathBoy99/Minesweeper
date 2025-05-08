
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
# Scale image to fit grid nicely with a smaller size
scale_factor = 0.5  # Adjust this value between 0 and 1 to change image size
scaled_width = int((screen.get_width() // grid_width) * scale_factor)
scaled_height = int((screen.get_height() // grid_length) * scale_factor)
image = pygame.transform.scale(image, (scaled_width, scaled_height))

# Calculate padding to center the grid
x_padding = (screen.get_width() - (scaled_width * grid_width)) // 2
y_padding = (screen.get_height() - (scaled_height * grid_length)) // 2

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
            x = x_padding + (col * scaled_width)
            y = y_padding + (row * scaled_height)
            screen.blit(image, (x, y))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
