import pygame
pygame.init()
WIDTH = 800
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
screen.fill("White")
pygame.display.update()
Fortnite = pygame.image.load("Pygame/images/adidas.png")
Roblox =pygame.image.load("Pygame/images/nike.png")
SubwaySurfers = pygame.image.load("Pygame/images/puma.png")
TempleRun = pygame.image.load("Pygame/images/jordan.png")
screen.blit(Fortnite,(10,10))
screen.blit(Roblox,(10,230))
screen.blit(SubwaySurfers,(10,430))
screen.blit(TempleRun,(10,660))
font = pygame.font.SysFont("Times New Roman",36)
text = font.render("Adidas",True,(0,0,0))
text1 = font.render("Nike",True,(0,0,0))
text2 = font.render("Puma",True,(0,0,0))
text3 = font.render("Jordan",True,(0,0,0))
screen.blit(text2,(350,100))
screen.blit(text3,(350,300))
screen.blit(text1,(350,500))
screen.blit(text,(350,700))

pygame.display.update()
while run:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(pos),30,30)
        pygame.display.update()
    elif event.type ==pygame.MOUSEBUTTONUP:
        pos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),(pos),(pos1),15)
        pygame.draw.circle(screen,(0,0,0),(pos1),30,30)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 