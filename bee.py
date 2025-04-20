import pygame
from pygame.locals import *
from time import *
pygame.init()
WIDTH = 800
HEIGHT = 800
keys = [False,False,False,False]
bee_x = 400
bee_y = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
grass=pygame.image.load("Pygame/images/grass.png")
bee=pygame.image.load("Pygame/images/bee.png")
run = True
while bee_y <800:
    screen.blit(grass,(0,0))
    screen.blit(bee,(bee_x,bee_y))
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
        if bee_y>0:
            bee_y -= 7
    if keys[2]:
        if bee_y<800:
            bee_y += 5
    if keys[1]:
        if bee_x>0:
            bee_x -= 5
    if keys[3]:
        if bee_x<800:
            bee_x += 5
    bee_y += 4
    sleep (0.05)
print("GameOver")
        