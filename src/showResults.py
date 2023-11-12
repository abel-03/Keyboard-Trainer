import pygame
import sys
import src.colors as colors
from src.textToScreen import text_to_screen 
from src.constants import *

def showResults(self):
    self.screen.blit(self.background, (0, 0))
    if self.points > self.record:
        self.setted_record = True
    if self.setted_record:
        self.record = self.points
        with open('txt/record', 'w') as f:
            f.write(str(self.points))
        self.score_height = self.HEIGHT * SCORE_HEIGHT_FACTOR
        self.mistakes_height = self.HEIGHT * MISTAKES_HEIGHT_FACTOR
        self.points_height = self.HEIGHT * POINTS_HEIGHT_FACTOR
        self.points_size = FONT_SIZE_RES
        text_to_screen(self, "НОВЫЙ РЕКОРД!", NEW_RECORD_TEXT_POSITION, FONT_SIZE_NEW_RECORD, colors.yellow, True)
    else:
        self.score_height = self.HEIGHT * SCORE_HEIGHT_FACTOR_ALT
        self.mistakes_height = self.HEIGHT * MISTAKES_HEIGHT_FACTOR_ALT
        self.points_height = self.HEIGHT * POINTS_HEIGHT_FACTOR_ALT
        self.points_size = FONT_SIZE_POINTS
    text_to_screen(self, f"Символов в минуту : {str(self.points)}", (self.WIDTH / 2, self.points_height), self.points_size, colors.blue, True)
    text_to_screen(self, f"Процент точности: {str(round(self.score / (self.mistakes + self.score) * 100, 2))}%", (self.WIDTH / 2, self.HEIGHT * PERCENT_HEIGHT_FACTOR), FONT_SIZE_RES, colors.green, True)
    # text_to_screen(self, f"Символы : {str(self.score)}", (self.WIDTH / 2, self.score_height), FONT_SIZE_RES, colors.blue, True)
    text_to_screen(self, f"Промахи : {str(self.mistakes)}", (self.WIDTH / 2, self.mistakes_height), FONT_SIZE_RES, colors.red, True)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.game_status = 'begining'        
