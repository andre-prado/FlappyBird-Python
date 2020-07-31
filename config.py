import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

BACKGROUND = pygame.image.load('assets/background-day.png');
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

SPEED = 10
GRAVITY = 1
