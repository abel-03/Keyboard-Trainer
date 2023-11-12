import time
import pygame
import sys

def typingProcess(self):
    self.start_time = time.time()
    self.input_text = ''
    self.right_input_lenght = 0
    self.mistakes = 0
    self.score = 0
    self.text = self.GetText()
    while time.time() - self.start_time <= self.playing_time:
        self.screen.blit(self.playing_background, (0, 0))
        self.showText()
        self.showTypedText()
        self.showTimer()
        self.showScore()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_status = 'begining'
                    return
                elif event.key == pygame.K_BACKSPACE:
                    if self.right_input_lenght == len(self.input_text) and self.right_input_lenght > 0:
                        self.right_input_lenght -= 1
                        self.score -= 1
                    self.input_text = self.input_text[:-1]
                else:
                    try:
                        self.input_text += event.unicode
                        if self.input_text[-1] == self.text[self.right_input_lenght] and self.right_input_lenght + 1 == len(self.input_text):
                            self.right_input_lenght += 1
                            self.score += 1
                        else:
                            self.mistakes += 1
                            self.input_text = self.input_text[:-1]
                    except:
                        pass
                if self.text == self.input_text:
                    self.text = self.GetText()
                    self.input_text = ''
                    self.right_input_lenght = 0
    self.save_result()
    self.setted_record = False
    self.game_status = 'showing_results'