import pygame

from const import *
from square import *
from piece import *


class Board(pygame.Surface):
    def __init__(self, board_width, board_height):
        super().__init__((board_width, board_height))
        self.squares = []
        self._create()
        self.coords = None
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_pawn, 1, Knight(color))
        self.squares[row_other][6] = Square(row_pawn, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_pawn, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_pawn, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_pawn, 0, Rook(color))
        self.squares[row_other][7] = Square(row_pawn, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_pawn, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_pawn, 4, King(color))

        print(self.squares)

    def calc_moves(self, piece, row, col):
        """Calculate all the possible moves of specific piece
        on a specific position"""

        if isinstance(piece, Pawn):
            pass
        elif isinstance(piece, Knight):
            pass
        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass

