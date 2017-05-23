import pygame
from enum import Enum


class PieceType(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    T = 6
    Z = 7


class Piece:
    def __init__(self, piece_type):
        self.piece_type = piece_type
        self.squares = []
        if piece_type == PieceType.I:
            top = 0
            for x in range (4):
                square = pygame.Rect(0, top, 30, 30)
                self.squares.append(square)
                top += 30
            self.color = pygame.Color("#600909")