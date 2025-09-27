import pygame
from PIL import Image, ImageDraw

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Pillow & Pygame Animation")

# Generate animation frames with Pillow
frames = []
for i in range(30):
    img = Image.new("RGB", (200, 200), "black")
    draw = ImageDraw.Draw(img)
    draw.rectangle((i * 5, 50, i * 5 + 50, 100), fill="blue")
    frames.append(img)

# Convert Pillow frames to Pygame surfaces
pygame_frames = [
    pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode) for frame in frames
]

# Main loop to display frames
running = True
frame_index = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the current frame
    screen.blit(pygame_frames[frame_index], (0, 0))
    frame_index = (frame_index + 1) % len(pygame_frames)  # Loop through frames

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(20)  # 10 frames per second

# Quit Pygame
pygame.quit()
