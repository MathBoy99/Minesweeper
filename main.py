
import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Grid")

# Grid dimensions (you can modify this)
grid_size = 3  # Size of the square grid (e.g., 3x3)

# Load the image
image = pygame.image.load('Untitled design (7).png')
# Scale image to fit grid nicely with a smaller size
scale_factor = 0.5  # Adjust this value between 0 and 1 to change image size
cell_width = screen.get_width() // grid_size
cell_height = screen.get_height() // grid_size
# Use the smaller dimension to maintain aspect ratio
cell_size = min(cell_width, cell_height)
scaled_size = int(cell_size * scale_factor)
image = pygame.transform.scale(image, (scaled_size, scaled_size))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill((0, 120, 120))
    
    # Draw grid of images
    for row in range(grid_size):
        for col in range(grid_size):
            x = col * scaled_size
            y = row * scaled_size
            screen.blit(image, (x, y))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
