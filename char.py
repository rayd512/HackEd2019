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
        self.rect.bottom = 250
        self.score = 0
        self.jumpwait = 0
        self.animation = 1
        self.animationtimer = 0
        self.isJump = 0
        self.NextJump = 40
        self.oldY = 0
        self.vel = 8
        self.mass = 2
    def update(self, WIDTH, HEIGHT, player, group2):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and self.isJump == 0 and self.NextJump > 40:
            self.isJump = 1
        if self.isJump == 1:
            self.animation = 0
            if self.vel > 0:
                self.rect.y -= 0.5*self.mass*(self.vel**2)
            else:
                self.rect.y += 0.5*self.mass*(self.vel**2)
            for texts in group2:
                if self.rect.bottom == texts.rect.top:
                    self.isJump = 0
                    self.animation = 1
                    self.vel = 8
                elif self.rect.top == texts.rect.bottom:
                    self.vel = 0
            self.vel -= 1
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
        self.NextJump += 0.75