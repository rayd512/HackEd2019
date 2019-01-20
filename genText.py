import pygame, colors
from pygame.locals import Color
class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, colour, size): 
        pygame.sprite.Sprite.__init__(self)
        self.FONT = pygame.freetype.SysFont('garamond', size)
        txt, rect = self.FONT.render(text, (255,255,255))
        WIDTH = txt.get_width()
        HEIGHT = txt.get_height()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(colour)
        # A pygame.Rect will serve as the blit position.
        self.rect = self.image.get_rect()
        # Render the text.
        
        # This txt_rect is used to center the text on the image.
        
        txt_rect_old = txt.get_rect()

        self.image = pygame.Surface((txt_rect_old.width, txt_rect_old.height))
        self.image.fill(colour)
        # A pygame.Rect will serve as the blit position.
        self.rect = self.image.get_rect()

        txt_rect = txt.get_rect(center=self.rect.center)
        self.image.blit(txt, txt_rect)
        # Set the position of the image rect.
        self.rect.topleft = x, y
    def update(self, SCROLL_SPEED):
        self.rect.x -= SCROLL_SPEED