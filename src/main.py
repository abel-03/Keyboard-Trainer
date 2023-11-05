import time
import pygame
from pygame.locals import *
import colors
from showFirstScreen import showFirstScreen
from textToScreen import text_to_screen
from typingProcess import typingProcess
from showResults import showResults
from makeLines import makeLines
from datetime import datetime
from showScores import showScores

class KeyboardTrainer:
    def __init__(self):
        self.WIDTH = 1500
        self.HEIGHT = 800

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Клавиатурный тренажер")
        self.clock = pygame.time.Clock()
        self.playing_time = 60

        self.background = pygame.image.load('Image/background.png')
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.playing_background = pygame.image.load('Image/playing_background.jpg')
        self.playing_background = pygame.transform.scale(self.playing_background, (self.WIDTH, self.HEIGHT))

        self.textCoordinates = (50, 150)

        makeLines(self)
        self.results = [line for line in open('txt/results').read().split('\n') if line != '']
        with open('txt/record') as f:
            self.record = int(f.read())

    def GetText(self):
        self.line_number += 1
        return self.lines[self.line_number]

    def showText(self):
        text_to_screen(self, self.text, self.textCoordinates)
        text_to_screen(self, self.text[:self.right_input_lenght], self.textCoordinates, 50, colors.black)

    def showTypedText(self):
        text_to_screen(self, self.input_text, (50, 250), 50, colors.red)
        text_to_screen(self, self.input_text[:self.right_input_lenght], (50, 250))

    def showTimer(self):
        self.timer = int(int(time.time() - self.start_time))
        text_to_screen(self, str(self.timer), (50, 50))

    def showScore(self):
        text_to_screen(self, str(self.mistakes), (1400, 50), 50, colors.red)
        text_to_screen(self, str(self.score), (1400, 100), 50, colors.blue)

    def rect_to_screen(self, color, left_border, up_border, width, height, border_width = 0):
        pygame.draw.rect(self.screen, color, (left_border, up_border, width, height), border_width)

    def show_start_buttom(self):
        self.rect_to_screen((255, 192, 203), self.WIDTH * 11 / 40, self.HEIGHT / 4, self.WIDTH * 18 / 40, 120, 4)
        text_to_screen(self, 'НАЧАТЬ', (self.WIDTH / 2, self.HEIGHT / 4 + 60), 120, colors.green, True)

    def show_scores_buttom(self):
        self.rect_to_screen((255, 192, 203), self.WIDTH / 3, self.HEIGHT * 23 / 40, self.WIDTH / 3, 70, 4)
        text_to_screen(self, 'РЕЙТИНГ', (self.WIDTH / 2, self.HEIGHT * 13 / 21), 70, colors.gray, True)

    def reset_results(self):
        open('txt/results', 'w').close()
        with open('txt/record', 'w') as f:
            f.write('0')
        self.record = 0
        self.results = []

    def save_result(self):
        self.current_time = datetime.now().strftime('%d/%m/%Y    %H:%M')
        self.points = max(0, self.score * 3 - self.mistakes * 7)
        self.results.append(f'{self.current_time}    {self.points}')
        with open('txt/results', 'a') as f:
            f.write(f'{self.results[-1]}\n')


    def show_reset_buttom(self):
        self.rect_to_screen(colors.black, self.WIDTH / 14, self.HEIGHT / 14, self.WIDTH / 3, 40, 4)
        text_to_screen(self, 'Удалить результаты', (self.WIDTH * 29 / 120, self.HEIGHT / 14 + 20), 40, colors.red, True)
    
    def run(self):
        self.running = True
        self.game_status = 'begining'
        while self.running:
            if self.game_status == 'begining':
                showFirstScreen(self)
            elif self.game_status == 'quit':
                self.running = False
            elif self.game_status == 'playing':
                typingProcess(self)
            elif self.game_status == 'showing_scores':
                showScores(self)
            elif self.game_status == 'showing_results':
                showResults(self)
            pygame.display.update()


KeyboardTrainer().run()