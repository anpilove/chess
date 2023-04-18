import sys
import pygame

pygame.init()

class Chess:
    def __init__(self):
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.clock = pygame.time.Clock()
        self.FPS = 30
        # Поработать над размерами окна
        self.game_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT),
                                                   pygame.RESIZABLE)
        pygame.display.set_caption("Chess")
        pygame.display.set_icon(pygame.image.load("icon.png"))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(self.FPS)


App = Chess()
App.run()










