import pygame
from PIL import Image

# Initialize Pygame
pygame.init()

# Load the animated GIF using Pillow
gif = Image.open("animations_gif/expanding_border.gif")

frames = []
# Get the duration of each frame (in milliseconds)
frame_duration = gif.info['duration']

# Extract frames from the GIF
try:
    while True:
        frame = gif.copy().convert("RGBA")
        frame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        frames.append(frame)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

# Set up the screen (window)
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RAHHHHHHH")
square = pygame.image.load("images_py/square.png")
square_x = 50
square_y = 50
square_mx = 5
square_my = 5

class Rect:
    def __init__(self, color, width, height, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.velocity = 3  # Speed of the chasing square

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self, target_x, target_y):
        # Calculate the direction vector towards the target
        direction_x = target_x - self.x
        direction_y = target_y - self.y
        distance = (direction_x**2 + direction_y**2) ** 0.5

        # Normalize the direction vector and update the position
        if distance != 0:
            self.x += self.velocity * (direction_x / distance)
            self.y += self.velocity * (direction_y / distance)

# Create a Rect object
rect = Rect(color=(255, 255, 0), width=50, height=50, x=5, y=5)

# Main loop
running = True
clock = pygame.time.Clock()
frame_index = 0
play_gif = False  # Flag to control GIF playback
show_rect = False  # Flag to control the visibility of the yellow square

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the window
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_gif = not play_gif  # Toggle GIF playback when spacebar is pressed
                show_rect = not show_rect  # Toggle the visibility of the yellow square

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_y -= square_my
    if keys[pygame.K_s]:
        square_y += square_my
    if keys[pygame.K_d]:
        square_x += square_mx
    if keys[pygame.K_a]:
        square_x -= square_mx

    screen.fill((0, 0, 0))

    if play_gif:
        # Calculate the position to center the GIF on the square
        gif_x = square_x + (square.get_width() - frames[frame_index].get_width()) // 2
        gif_y = square_y + (square.get_height() - frames[frame_index].get_height()) // 2
        screen.blit(frames[frame_index], (gif_x, gif_y))
        # Update the frame index
        frame_index = (frame_index + 1) % len(frames)

    # Blit the square image
    screen.blit(square, (square_x, square_y))

    # Update the rect's position to chase the square
    rect.update(square_x, square_y)
    
    # Draw the rect if visible
    if show_rect:
        rect.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Control the frame rate

# Quit Pygame
pygame.quit()