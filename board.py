from pygame import font

from conf import *

import pygame

class Board:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 50)

    def draw(self, screen, matrix):
        screen.fill(GRID_COLOR)
        for row in range(GRID):
            for col in range(GRID):
                value = matrix.matrix[row][col]

                color = CELL_COLOR.get(value)

                pos_y = MARGIN + col * CELL_SIZE + SPACE_BETWEEN * col
                pos_x = MARGIN + row * CELL_SIZE + SPACE_BETWEEN * row
                pygame.draw.rect(
                    screen,
                    color,
                    (pos_y, pos_x, CELL_SIZE, CELL_SIZE),
                    border_radius=5,
                )
                if value != 0:
                    text = self.font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(pos_y + CELL_SIZE // 2, pos_x + CELL_SIZE // 2))
                    screen.blit(text, text_rect)

    def game_over(self, screen, score):

        if score == MAX_SCORE:
            end_text = "You Win!"
        else:
            end_text = "Game Over"

        overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        overlay.set_alpha(200)
        overlay.fill((245, 235, 191))
        screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render(end_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 30))
        screen.blit(text, text_rect)

        score_font = pygame.font.Font(None, 50)
        score_text = score_font.render(f"Your Score: {score}", True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 + 30))
        screen.blit(score_text, score_rect)

        pygame.display.flip()

    def game_win(self, screen):
        pass