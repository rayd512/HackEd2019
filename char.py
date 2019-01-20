import pygame, colors

class Char(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.images_default = [pygame.image.load("Trump/6.png"),
        pygame.image.load("Trump/7.png"),
        pygame.image.load("Trump/8.png"),
        pygame.image.load("Trump/9.png"),
        pygame.image.load("Trump/10.png"),
        pygame.image.load("Trump/11.png")] 
        self.image = self.images_default[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = HEIGHT - 153
        self.score = 0
        self.jumpwait = 0
        self.animation = 1
        self.animationtimer = 0
        self.inJump = 0
        self.NextJump = 40
    def update(self, WIDTH, HEIGHT):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and self.inJump == 0 and self.NextJump > 40:
            self.jumpwait = 0
            self.rect.y = HEIGHT - 200
            self.animation = 0
            self.inJump = 1
            self.NextJump = 0

        
        if self.jumpwait > 40:
            self.rect.y += 9.81
            if self.rect.y >= HEIGHT - 153:
                self.animation = 1
                self.inJump = 0
                self.jumpwait = 0
        
        if self.animation == 1:
            if self.animationtimer == 60:
                self.image = self.images_default[4]
                self.animationtimer = 0
            elif self.animationtimer == 54:
                self.image = self.images_default[3]
            elif self.animationtimer == 48:
                self.image = self.images_default[2]
            elif self.animationtimer == 42:
                self.image = self.images_default[1]
            elif self.animationtimer == 36:
                self.image = self.images_default[0]
            elif self.animationtimer == 30:
                self.image = self.images_default[5]
            elif self.animationtimer == 24:
                self.image = self.images_default[4]
            elif self.animationtimer == 18:
                self.image = self.images_default[3]
            elif self.animationtimer == 12:
                self.image = self.images_default[2]
            elif self.animationtimer == 6:
                self.image = self.images_default[1]
            elif self.animationtimer == 0:
                self.image = self.images_default[0]
            self.animationtimer += 1
        if self.rect.y == HEIGHT - 200:
            self.jumpwait += 1
        self.NextJump += 0.75