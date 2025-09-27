import pygame
import sys

pygame.init()
FPS = 60
running = True
screen_width, screen_height = 800, 600
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("aaaaaaaaaa")

# Define tabs
TABS = ["Tab1", "Tab2", "Tab3"]
tab_colors = [black, green, white]
current_tab = 0

def draw_tab_background():
    screen.fill(tab_colors[current_tab])

# Moving box properties
box_pos = [100, 100]
box_speed = 5

def draw_moving_box():
    pygame.draw.rect(screen, white, (*box_pos, 50, 50))

rects = []

# The Box
button_inv = pygame.Rect(0, 0, 100, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at:", event.pos)  # Debug print
            if button_inv.collidepoint(event.pos):
                print("Button clicked! Creating new rectangle")  # Debug print
                new_rect = pygame.Rect(500, 600, 275, 100)
                rects.append(new_rect)
        


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        box_pos[0] -= box_speed
    if keys[pygame.K_d]:
        box_pos[0] += box_speed
    if keys[pygame.K_w]:
        box_pos[1] -= box_speed
    if keys[pygame.K_s]:
        box_pos[1] += box_speed

    draw_tab_background()
    pygame.draw.rect(screen, white, button_inv)
    for i, rect in enumerate(rects):
        print(f"Drawing rectangle {i} at:", rect.topleft)  # Debug print
        pygame.draw.rect(screen, white, rect)
        
    if current_tab == 0:  # Moving box only in Tab1
        draw_moving_box()

    pygame.display.flip()
    clock.tick(FPS)
