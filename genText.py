import pygame, colors

class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, colour): 
        pygame.sprite.Sprite.__init__(self)
        self.FONT = pygame.font.SysFont('garamond', 60)

        # Render the text.
        txt = self.FONT.render(text, True, colors.white)
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
    def update(self):
        self.rect.x -= 1