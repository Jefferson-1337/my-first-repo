import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tabbed Interface with Moving Box")
clock = pygame.time.Clock()

# Define tabs
TABS = ["Tab1", "Tab2", "Tab3"]
tab_colors = [RED, GREEN, BLUE]
current_tab = 0

# Moving box properties
box_pos = [100, 100]
box_speed = 5

def draw_tab_background():
    screen.fill(tab_colors[current_tab])

def draw_tabs():
    for index, tab in enumerate(TABS):
        tab_rect = pygame.Rect(index * (SCREEN_WIDTH // len(TABS)), 0, SCREEN_WIDTH // len(TABS), 50)
        pygame.draw.rect(screen, WHITE, tab_rect, 2)
        tab_text = pygame.font.SysFont(None, 36).render(tab, True, WHITE)
        screen.blit(tab_text, (tab_rect.x + 10, tab_rect.y + 10))

def draw_moving_box():
    pygame.draw.rect(screen, WHITE, (*box_pos, 50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mouse_y <= 50:
                current_tab = mouse_x // (SCREEN_WIDTH // len(TABS))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_pos[0] -= box_speed
    if keys[pygame.K_RIGHT]:
        box_pos[0] += box_speed
    if keys[pygame.K_UP]:
        box_pos[1] -= box_speed
    if keys[pygame.K_DOWN]:
        box_pos[1] += box_speed

    draw_tab_background()
    draw_tabs()
    if current_tab == 0:  # Moving box only in Tab1
        draw_moving_box()

    pygame.display.flip()
    clock.tick(FPS)
