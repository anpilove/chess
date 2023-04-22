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
        dragger = self.game.dragger
        board = self.game.board

        screen.fill(color="gray")
        game.draw_board(screen)
        game.draw_pieces(screen)
        while True:
            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    pygame.mouse.get_pos()
                    for row in range(ROWS):
                        for col in range(COLS):
                            if board.squares[row][col].true_coords.collidepoint(event.pos):
                                print(row, col)


                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # click release
                elif event.type == pygame.MOUSEMOTION:
                    pass

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(self.FPS)


App = Chess()
App.run()
