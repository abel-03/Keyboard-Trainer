import colors
import pygame

def text_to_screen(self, text, coordinates, size = 50,
            color = colors.white, center = False, font_type = None):
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    if center:
        text_rect = text.get_rect(center = coordinates)
        self.screen.blit(text, text_rect)
        return
    self.screen.blit(text, coordinates)