import pygame
import time
import math
pygame.init()
WIDTH = 800
HEIGHT = 800
pygame.display.set_caption("Asteroid Game")
background = pygame.image.load("Pygame/images/space3.png")
spaceship = pygame.image.load("Pygame/images/bluespaceship.png")
Sasteroid = pygame.image.load("Pygame/images/smallasteroid.png")
Masteroid = pygame.image.load("Pygame/images/bigasteroid.png")
Lasteroid = pygame.image.load("Pygame/images/largeasteroid.png")
ufo = pygame.image.load("Pygame/images/ufo.png")
star = pygame.image.load("Pygame/images/whitecomet.png")
GameOver = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def Redraw_gamewindow():
    screen.blit(background,(0,0))
    player.draw(screen)
    for b in player_bullets:
        b.draw(screen)
    pygame.display.update()
class Player():
    def __init__(self):
        self.image = spaceship
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y + self.sine * self.h // 2)
    def turn_left(self):
        self.angle += 5
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y + self.sine * self.h // 2)
    def turn_right(self):
        self.angle -= 5
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y + self.sine * self.h // 2)
    def forward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y + self.sine * self.h // 2)
    def draw(self,screen):
        #screen.blit(self.image,[self.x,self.y,self.w,self.h])
        screen.blit(self.rotatedsurface,self.rotatedrect)

class Bullet():
    def __init__(self):
        self.point = player.head
        self.x,self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),[self.x,self.y,self.w,self.h])


player_bullets = []
player = Player()
run = True
while run:
    clock.tick(60)
    if not GameOver:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.forward()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not GameOver:
                    player_bullets.append(Bullet())
        if event.type == pygame.QUIT:
            pygame.quit()
    Redraw_gamewindow()