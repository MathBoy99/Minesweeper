
import pygame
import os

# Initialize Pygame
pygame.init()

def load_and_scale_image(image_name, cell_size, scale_factor=0.5):
  """Load and scale an image based on cell size and scale factor"""
  image = pygame.image.load(image_name)
  scaled_size = int(cell_size * scale_factor)
  return pygame.transform.scale(image, (scaled_size, scaled_size))
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Grid")

# Grid dimensions (you can modify this)
grid_size = 8  # Size of the square grid (e.g., 3x3)

# Calculate grid cell sizes
scale_factor = 0.5  # Adjust this value between 0 and 1 to change image size
cell_width = screen.get_width() // grid_size
cell_height = screen.get_height() // grid_size
cell_size = min(cell_width, cell_height)
scaled_size = int(cell_size * scale_factor)

# Load and scale the image
image = load_and_scale_image('Untitled design (7).png', cell_size, scale_factor)

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
