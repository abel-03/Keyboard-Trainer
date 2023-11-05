import pygame
import sys
import colors
from textToScreen import text_to_screen

def showScores(self):
    self.screen.blit(self.background, (0, 0))
    self.result_height = self.HEIGHT / 5
    text_to_screen(self, "Нажмите Esc для возвращения на главное меню", (self.WIDTH * 0.8, self.HEIGHT / 10), 30, colors.red, True)
    self.show_reset_buttom()
    text_to_screen(self, "ДАТА             ВРЕМЯ    ОЧКИ", (self.WIDTH / 10, self.result_height))
    for result in self.results[::-1]:
        self.result_height += 50
        text_to_screen(self, result, (self.WIDTH / 10, self.result_height), 50, colors.gray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_status = 'begining'
                return
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if x >= self.WIDTH / 14 and x <= self.WIDTH * (1 / 14 + 1 / 3) and y >= self.HEIGHT / 14 and y <= self.HEIGHT / 14 + 40:
                self.reset_results()
