import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350, 700))

bg_color = pygame.Color("#ffffff")

while True:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    pygame.display.update()
    pygame.time.delay(50)