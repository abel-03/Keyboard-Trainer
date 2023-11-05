import sys
import pygame

def showFirstScreen(self):
        self.text = 'НАЧАТЬ'
        self.screen.blit(self.background, (0, 0))
        self.show_start_buttom()
        self.show_scores_buttom()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if x >= self.WIDTH * 11 / 40 and x <= self.WIDTH * 29 / 40 and y >= self.HEIGHT / 4 and y <= self.HEIGHT / 4 + 120:
                    self.game_status = 'playing'
                elif x >= self.WIDTH / 3 and x <= self.WIDTH * 2 / 3 and y >= self.HEIGHT * 23 / 40 and y <= self.HEIGHT * 23 / 40 + 70:
                    self.game_status = 'showing_scores'