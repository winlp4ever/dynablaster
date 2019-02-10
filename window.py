import pygame
from PIL import Image
from pygame.locals import*


img = pygame.image.load('imgs/bomberman.png')
img = pygame.transform.scale(img, (100, 100))
print(type(img))

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))
    screen.blit(img,(240,240))
    pygame.display.flip()
