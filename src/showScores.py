import pygame
import sys
import src.colors as colors
from src.textToScreen import text_to_screen
from src.constants import *

def showScores(self):
    self.screen.blit(self.background, (0, 0))
    self.result_height = RESULT_HEIGHT
    text_to_screen(self, "Нажмите Esc для возвращения на главное меню", ESC_BUTTON_POSITION, ESC_TEXT_SIZE, colors.red, True)
    self.show_reset_buttom()
    text_to_screen(self, "ДАТА             ВРЕМЯ    ОЧКИ", (DATA_TIME_SCORE_POSITION_WIDTH, self.result_height))
    for result in self.results[::-1]:
        self.result_height += 50
        text_to_screen(self, result, (RESULT_BUTTON_POSITION_WIDTH, self.result_height), RESULT_TEXT_SIZE, colors.gray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_status = 'begining'
                return
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x >= RESET_BUTTON_LEFT and x <= RESET_BUTTON_RIGHT and y >= RESET_BUTTON_TOP and y <= RESET_BUTTON_BOTTOM:
                self.reset_results()
