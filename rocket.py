import pygame
from pygame.locals import *
from time import *
pygame.init()
WIDTH = 800
HEIGHT = 800
keys = [False,False,False,False]
rocket_x = 400
rocket_y = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
space=pygame.image.load("Pygame/images/space.png")
rocketship=pygame.image.load("Pygame/images/rocketship.png")
run = True
while rocket_y <800:
    screen.blit(space,(0,0))
    screen.blit(rocketship,(rocket_x,rocket_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_LEFT:
                keys[1]=False
            elif event.key==K_DOWN:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if rocket_y>0:
            rocket_y -= 7
    if keys[2]:
        if rocket_y<800:
            rocket_y += 5
    if keys[1]:
        if rocket_x>0:
            rocket_x -= 5
    if keys[3]:
        if rocket_x<800:
            rocket_x += 5
    rocket_y += 4
    sleep (0.05)
print("GameOver")
        