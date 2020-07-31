import pygame
import config

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('assets/bluebird-downflap.png').convert_alpha()]
        
        self.current_image = 0

        self.speed = config.SPEED

        self.image = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = config.SCREEN_WIDTH / 2
        self.rect[1] = config.SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        self.speed += config.GRAVITY
        # Update height
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -config.SPEED