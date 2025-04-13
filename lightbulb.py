import pygame
import time
import os
import sys
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("Pygame/images/lightoff.jpeg")
pygame.display.set_caption("Ligth Bulb Switcher")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
    screen.blit(img,(0,0))
    pygame.display.update()
    time.sleep(2)
    cake=pygame.image.load("Pygame/images/lighton.jpeg")
    screen.fill("black")
    screen.blit(cake,(0,0))
    pygame.display.update()
    time.sleep(2)