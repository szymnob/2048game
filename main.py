
import pygame
from board import Board
from matrix import Matrix

from conf import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("2048")
        self.running = True

        self.game_state = "continue"

        self.board = Board()

        self.matrix = Matrix(GRID)

    def restart(self):
        self.matrix = Matrix(GRID)
        self.running = True

        self.run()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.matrix.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.matrix.move_right()
                elif event.key == pygame.K_UP:
                    self.matrix.move_up()
                elif event.key == pygame.K_DOWN:
                    self.matrix.move_down()
                elif event.key == pygame.K_q:
                    pygame.quit()

    def game_over(self):
        self.board.draw(self.screen, self.matrix)
        if self.game_state == "lose":
            self.board.game_over(self.screen, self.matrix.get_max_value())
        elif self.game_state == "win":
            self.board.game_win(self.screen)

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.restart()


    def run(self):
        while self.running:
            self.handle_event()
            self.game_state = self.matrix.check_game_state()
            self.board.draw(self.screen, self.matrix)
            pygame.display.flip()

            if self.game_state != "continue":
                self.running = False

        self.game_over()



if __name__ == "__main__":
    game = Game()
    game.run()

