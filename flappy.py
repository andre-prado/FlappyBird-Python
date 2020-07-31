import pygame
from pygame.locals import *
from bird.bird import Bird
import config

screen_width = config.SCREEN_WIDTH
screen_heigth = config.SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))

background = config.BACKGROUND

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(background, (0, 0))

    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update()
