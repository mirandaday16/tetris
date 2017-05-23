import pygame
import sys
from objects import PieceType, Piece

pygame.init()
screen = pygame.display.set_mode((360, 720))

bg_color = pygame.Color("#ffffff")
piece = Piece(PieceType.I)
while True:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    for square in piece.squares:
        pygame.draw.rect(screen, piece.color, square)
        pygame.draw.rect(screen, pygame.Color("#000000"), square, 2)

    pygame.display.update()
    pygame.time.delay(50)