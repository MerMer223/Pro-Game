import pygame
import time
import math
import random
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
    for a in asteroids:
        a.draw(screen)
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
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
    def turn_left(self):
        self.angle += 5
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
    def turn_right(self):
        self.angle -= 5
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
    def forward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedsurface = pygame.transform.rotate(self.image,self.angle)
        self.rotatedrect = self.rotatedsurface.get_rect()
        self.rotatedrect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
    def draw(self,screen):
        #screen.blit(self.image,[self.x,self.y,self.w,self.h])
        screen.blit(self.rotatedsurface,self.rotatedrect)
    def updateLocation(self):
        if self.x > WIDTH + 50:
            self.x = 0
        elif self.x < 0 -self.w:
            self.x = WIDTH
        elif self.y < - 50:
            self.y = HEIGHT
        elif self.y > HEIGHT + 50:
            self.y = 0

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
    def checkOffScreen(self):
        if self.x < -50 or self.x > WIDTH or self.y > HEIGHT or self.y < -50: 
            return True
class Asteroid():
    def __init__(self,rank):
        self.rank = rank
        if self.rank == 1:
            self.image = Sasteroid
        elif self.rank == 2:
            self.image = Masteroid
        else:
            self.image = Lasteroid
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0,WIDTH - self.w),random.choice([-1*self.h-5,HEIGHT + 5])),(random.choice([-1*self.w - 5, WIDTH + 5]),random.randrange(0, HEIGHT - self.h))])
        self.x,self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self. y < HEIGHT // 2:
            self.ydir =1
        else: self.ydir = -1
        self.xv = self.xdir *random.randrange(1,3)
        self.yv = self.ydir *random.randrange(1,3)
    def draw(self, screen):
        screen.blit(self.image,(self.x,self.y))
asteroids = []
count = 0




player_bullets = []
player = Player()
run = True
while run:
    clock.tick(60)
    count += 1
    if not GameOver:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        player.updateLocation()
        for b in player_bullets:
            b.move()
            if b.checkOffScreen():
                player_bullets.pop(player_bullets.index(b))
        for a in asteroids:
            a.x += a.xv
            a.y += a.yv
        
            for b in player_bullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x +b.w <= a.x +a.w:
                    if (b.y >= a.y and b.y <= a.y +a.h) or b.y >= b.h >= a.y and b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y =a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y =a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        asteroids.pop(asteroids.index(a))
                        player_bullets.pop(player_bullets.index(b))
                        
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