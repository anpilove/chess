import pygame
from const import *
from board import *
from dragger import *

class Game:
    def __init__(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        self.dragger = Dragger()

    def draw_board(self, surface: pygame.surface):
        self.board.coords = self.board.get_rect(center=surface.get_rect().center)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = COLOR_LIGHT
                else:
                    color = COLOR_DARK
                rect = (col * SIZE_SQ, row * SIZE_SQ, SIZE_SQ, SIZE_SQ)
                self.board.squares[row][col].coords = pygame.draw.rect(self.board, color, rect)
                self.board.squares[row][col].true_coords = pygame.Rect(
                    (self.board.coords.x + self.board.squares[row][col].coords.x,
                     self.board.coords.y + self.board.squares[row][col].coords.y),
                    self.board.squares[row][col].coords.size)
        surface.blit(self.board, self.board.coords)

    def draw_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    img = pygame.image.load(piece.texture)
                    img_center = self.board.squares[row][col].coords.center
                    piece.texture_rect = img.get_rect(center=img_center)
                    self.board.blit(img, piece.texture_rect)

        rect = self.board.get_rect(center=surface.get_rect().center)
        surface.blit(self.board, rect)


