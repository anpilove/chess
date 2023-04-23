import sys
import pygame
from const import *
from game import *
from board import *


class Chess:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        # Поработать над размерами окна
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chess")
        pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    def run(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        screen.fill(color="gray")
        game.draw_board(screen)
        game.draw_pieces(screen)

        while True:

            for event in pygame.event.get():
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    for row in range(ROWS):
                        for col in range(COLS):
                            if board.squares[row][col].true_coords.collidepoint(event.pos):
                                clicked_row = row
                                clicked_col = col

                                # if clicked square has a piece ?
                                if board.squares[clicked_row][clicked_col].has_piece():
                                    piece = board.squares[clicked_row][clicked_col].piece
                                    dragger.save_initial(clicked_row, clicked_col)
                                    dragger.drag_piece(piece)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        screen.fill(color="gray")
                        game.draw_board(screen)
                        game.draw_pieces(screen)
                        dragger.update_blit(screen, board)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                    screen.fill(color="gray")
                    game.draw_board(screen)
                    game.draw_pieces(screen)

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(self.FPS)


App = Chess()
App.run()
