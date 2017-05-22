# I, J, L, O, S, T, Z
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
        