import pygame
import sys
import colors
from textToScreen import text_to_screen

def showResults(self):
    self.screen.blit(self.background, (0, 0))
    if self.points > self.record:
        self.setted_record = True
    if self.setted_record:
        self.record = self.points
        with open('txt/record', 'w') as f:
            f.write(str(self.points))
        self.score_height = self.HEIGHT * 13 / 20
        self.mistakes_height = self.HEIGHT * 16 / 20
        self.points_height = self.HEIGHT * 10 / 20
        self.points_size = 70
        text_to_screen(self, "НОВЫЙ РЕКОРД!", (self.WIDTH / 2, self.HEIGHT / 3), 100, colors.yellow, True)
    else:
        self.score_height = self.HEIGHT * 3 / 5
        self.mistakes_height = self.HEIGHT * 4 / 5
        self.points_height = self.HEIGHT / 3
        self.points_size = 100
    text_to_screen(self, f"Очки : {str(self.points)}", (self.WIDTH / 2, self.points_height), self.points_size, colors.blue, True)
    text_to_screen(self, f"Символы : {str(self.score)}", (self.WIDTH / 2, self.score_height), 70, colors.blue, True)
    text_to_screen(self, f"Промахи : {str(self.mistakes)}", (self.WIDTH / 2, self.mistakes_height), 70, colors.red, True)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.game_status = 'begining'        
