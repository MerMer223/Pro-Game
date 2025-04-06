import pygame
import time
import os
import sys
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("Pygame/images/birthday.jpeg")
pygame.display.set_caption("Birthday Greeting Card")
run = True
while run:
    font=pygame.font.SysFont("Times New Roman",72)
    text=font.render("Happy",True,(0,0,0))
    text2=font.render("Birthday",True,(0,0,0))
    text3=font.render("Wish You A",True,(0,0,0))
    text4=font.render("Bright Future",True,(0,0,0))
    text5=font.render("Ahead",True,(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
    screen.blit(img,(0,0))
    screen.blit(text,(400,100))
    screen.blit(text2,(400,160))
    pygame.display.update()
    time.sleep(2)
    cake=pygame.image.load("Pygame/images/cake.jpeg")
    screen.fill("white")
    screen.blit(cake,(0,0))
    screen.blit(text3,(350,50))
    screen.blit(text4,(350,110))
    screen.blit(text5,(350,170))
    pygame.display.update()
    time.sleep(2)