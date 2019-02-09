import pygame,sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURE = pygame.display.set_mode((800,500),0,32)
pygame.display.set_caption("Hello World!")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

btn = pygame.image.load("cat.png")
catx = 10
caty = 10

direction = "right"

while True:
    DISPLAYSURE.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 680:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 420:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURE.blit(btn, (catx, caty))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)