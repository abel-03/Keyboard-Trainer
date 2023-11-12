import sys
import pygame
from src.constants import *


def showFirstScreen(self):
    self.text = "НАЧАТЬ"
    self.screen.blit(self.background, (0, 0))
    self.show_start_buttom()
    self.show_scores_buttom()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if (
                x >= START_BUTTON_X_START
                and x <= START_BUTTON_X_END
                and y >= START_BUTTON_Y_START
                and y <= START_BUTTON_Y_END
            ):
                self.game_status = "playing"
            elif (
                x >= SCORES_BUTTON_X_START
                and x <= SCORES_BUTTON_X_END
                and y >= SCORES_BUTTON_Y_START
                and y <= SCORES_BUTTON_Y_END
            ):
                self.game_status = "showing_scores"
