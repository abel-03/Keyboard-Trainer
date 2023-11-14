import time
import pygame
from pygame.locals import *
import src.colors as colors
from src.textToScreen import text_to_screen
from src.makeLines import makeLines
from datetime import datetime
from src.constants import *

class KeyboardTrainer:
    def __init__(self):
        pygame.init()
        
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Клавиатурный тренажер")
        self.clock = pygame.time.Clock()
        self.playing_time = PLAYING_TIME

        self.background = pygame.image.load(BACKGROUND_IMAGE_PATH)
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.playing_background = pygame.image.load(PLAYING_BACKGROUND_PATH)
        self.playing_background = pygame.transform.scale(self.playing_background, (self.WIDTH, self.HEIGHT))

        self.textCoordinates = TEXT_COORDINATES

        makeLines(self)
        self.results = [line for line in open('txt/results').read().split('\n') if line != '']
        with open('txt/record') as f:
            self.record = int(f.read())

    def GetText(self):
        self.line_number += 1
        return self.lines[self.line_number]

    def showText(self):
        text_to_screen(self, self.text, self.textCoordinates)
        text_to_screen(self, self.text[:self.right_input_lenght], self.textCoordinates, LINE_HEIGHT, colors.black)

    def showTypedText(self):
        text_to_screen(self, self.input_text, TYPED_TEXT_COORDINATES, LINE_HEIGHT, colors.red)
        text_to_screen(self, self.input_text[:self.right_input_lenght], TYPED_TEXT_COORDINATES)

    def showTimer(self):
        self.timer = int(int(time.time() - self.start_time))
        text_to_screen(self, str(self.timer), TIMER_POSITION)

    def showScore(self):
        text_to_screen(self, str(self.mistakes), MISTAKES_POSITION, LINE_HEIGHT, colors.red)
        text_to_screen(self, str(self.score * 60 / self.playing_time), SCORE_POSITION, LINE_HEIGHT, colors.blue)
        if self.mistakes + self.score == 0:
            text_to_screen(self, str(100) + '%', SCORE_PERCENT_POSITION, LINE_HEIGHT, colors.blue)
        else:
            text_to_screen(self, str(round(self.score / (self.mistakes + self.score) * 100, 2))+ '%', SCORE_PERCENT_POSITION, LINE_HEIGHT, colors.blue)

    def rect_to_screen(self, color, left_border, up_border, width, height, border_width = 0):
        pygame.draw.rect(self.screen, color, (left_border, up_border, width, height), border_width)

    def show_start_buttom(self):
        self.rect_to_screen( colors.pink, START_BUTTON_POSITION_WIDTH, START_BUTTON_POSITION_HEIGHT, START_BUTTON_SIZE_WIDTH, START_BUTTON_SIZE_HEIGHT, BORDER_WIDTH)
        text_to_screen(self, 'НАЧАТЬ', START_BUTTON_TEXT_POSITION, START_BUTTON_TEXT_SIZE, colors.green, True)

    def show_scores_buttom(self):
        self.rect_to_screen( colors.pink, SCORES_BUTTON_POSITION_WIDTH, SCORES_BUTTON_POSITION_HEIGHT, SCORES_BUTTON_SIZE_WIDTH, SCORES_BUTTON_SIZE_HEIGHT, BORDER_WIDTH)
        text_to_screen(self, 'РЕЙТИНГ', SCORES_BUTTON_TEXT_POSITION, SCORES_BUTTON_TEXT_SIZE, colors.gray, True)

    def reset_results(self):
        open('txt/results', 'w').close()
        with open('txt/record', 'w') as f:
            f.write('0')
        self.record = 0
        self.results = []

    def save_result(self):
        self.current_time = datetime.now().strftime('%d/%m/%Y    %H:%M')
        self.points = int(self.score * 60 / self.playing_time)
        self.results.append(f'{self.current_time}    {self.points}')
        with open('txt/results', 'a') as f:
            f.write(f'{self.results[-1]}\n')


    def show_reset_buttom(self):
        self.rect_to_screen(colors.black, RESET_BUTTON_POSITION_WIDTH, RESET_BUTTON_POSITION_HEIGHT, RESET_BUTTON_SIZE_WIDTH, RESET_BUTTON_SIZE_HEIGHT, BORDER_WIDTH)
        text_to_screen(self, 'Удалить результаты', RESET_BUTTON_TEXT_POSITION, RESET_BUTTON_TEXT_SIZE, colors.red, True)
