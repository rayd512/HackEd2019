import pygame, colors
from pygame.locals import Color
class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, colour, size): 
        pygame.sprite.Sprite.__init__(self)
        self.FONT = pygame.freetype.SysFont('garamond', size)
        txt, rect = self.FONT.render(text, colors.black)
        WIDTH = txt.get_width()
        HEIGHT = txt.get_height()
        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
        self.image.fill((0,0,0,10))
        # A pygame.Rect will serve as the blit position.
        self.rect = self.image.get_rect()

        txt_rect = txt.get_rect(center=self.rect.center)
        self.image.blit(txt, txt_rect)
        # Set the position of the image rect.
        self.rect.topleft = x, y
    def update(self, SCROLL_SPEED, group):
        self.rect.x -= SCROLL_SPEED
        if self.rect.right <= 0:
            group.remove(self)