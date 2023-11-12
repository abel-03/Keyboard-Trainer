
import pygame
from pygame.locals import *
from src.showFirstScreen import showFirstScreen
from src.typingProcess import typingProcess
from src.showResults import showResults
from src.showScores import showScores
from src.runner import KeyboardTrainer


def main():
    game = KeyboardTrainer()
    game.running = True
    game.game_status = 'begining'
    while game.running:
        if game.game_status == 'begining':
            showFirstScreen(game)
        elif game.game_status == 'quit':
            game.running = False
        elif game.game_status == 'playing':
            typingProcess(game)
        elif game.game_status == 'showing_scores':
            showScores(game)
        elif game.game_status == 'showing_results':
            showResults(game)
        pygame.display.update()


if __name__ == '__main__':
    main()