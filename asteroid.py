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
shoot = pygame.mixer.Sound("Pygame/images/shoot.wav")
bangLargeSound = pygame.mixer.Sound("Pygame/images/bangLarge.wav")
bangSmallSound = pygame.mixer.Sound("Pygame/images/bangSmall.wav")

GameOver = False
lives = 3
score = 0
highScore = 0
rapidFire = False
rfStart = -1
isSoundOn = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def Redraw_gamewindow():
    screen.blit(background,(0,0))
    font = pygame.font.SysFont('arial',30)
    livesText = font.render('Lives:' + str(lives), 1,(255,255,255))
    playAgainText = font.render("Press Tab to Play Again", 1, (255,255,255))
    scoreText = font.render("Score:" + str(score), 1,(255,255,255))
    highScoreText = font.render("High Score: " + str(highScore), 1,(255,255,255))
    player.draw(screen)
    for b in player_bullets:
        b.draw(screen)
    for a in asteroids:
        a.draw(screen)
    for s in stars:
        s.draw(screen)
    for l in aliens:
        l.draw(screen)
    for u in  alien_bullets:
        u.draw(screen)
    if rapidFire:
        pygame.draw.rect(screen,(0,0,0), [WIDTH//2 - 51, 19, 102, 22])
        pygame.draw.rect(screen, (255,255,255), [WIDTH//2 - 50, 20, 100 - 100*(count - rfStart)/500,20])
    if GameOver:
        screen.blit(playAgainText, (WIDTH//2- playAgainText.get_width()//2 , HEIGHT//2 - playAgainText.get_height()//2))
    screen.blit(scoreText, (WIDTH - scoreText.get_width()- 25,25))
    screen.blit(livesText, (25,25))
    screen.blit(highScoreText, (WIDTH - highScoreText.get_width() - 25, 35 + scoreText.get_height()))
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

class Star():
    def __init__(self):
        self.img = star
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0,WIDTH - self.w),random.choice([-1*self.h-5,HEIGHT + 5])),(random.choice([-1*self.w - 5, WIDTH + 5]),random.randrange(0, HEIGHT - self.h))])
        self.x,self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))

class Alien():
    def __init__(self):
        self.img = ufo
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0,WIDTH - self.w),random.choice([-1*self.h-5,HEIGHT + 5])),(random.choice([-1*self.w - 5, WIDTH + 5]),random.randrange(0, HEIGHT - self.h))])
        self.x,self.y = self.ranPoint
        if self.x < WIDTH//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))

class Alien_bullet():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx,self.dy)
        self.dx , self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),[self.x,self.y,self.w,self.h])
        

player_bullets = []
asteroids = []
stars = []
aliens = []
alien_bullets = []
player = Player()
run = True
while run:
    clock.tick(60)
    count += 1
    if not GameOver:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        if count % 1000 == 0:
            stars.append(Star())
        if count % 750 == 0:
            aliens.append(Alien())
        for i, a in enumerate(aliens):
            a.x += a.xv
            a.y += a.yv
            if a.x > WIDTH + 150 or a.x + a.w < -100 or a.y > HEIGHT + 150 or a.y + a.h <- 100:
                aliens.pop(i)
            if count % 60 == 0:
                alien_bullets.append(Alien_bullet(a.x + a.w//2, a.y + a.h//2))   
            for b in player_bullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x +b.w <= a.x +a.w:
                    if (b.y >= a.y and b.y <= a.y +a.h) or b.y >= b.h >= a.y and b.y + b.h <= a.y + a.h:  
                        aliens.pop(i)
                        if isSoundOn:
                            bangLargeSound.play()
                        score += 50
                        break 
        for i, b in enumerate(alien_bullets):
            b.x += b.xv
            b.y += b.yv
            if (b.x >= player.x - player.w//2 and b.x <= player.x + player.w//2) or b.x + b.w >= player.x - player.w//2 and b.x + b.w <= player.x + player.w//2:
                if (b.y >= player.y - player.h//2 and b.y <= player.y + player.h//2) or b.y + b.h >= player.y - player.h//2 and b.y + b.h <= player.y + player.h//2:
                    lives -= 1
                    alien_bullets.pop(i)
                    break   
            
                        
        player.updateLocation()
        for b in player_bullets:
            b.move()
            if b.checkOffScreen():
                player_bullets.pop(player_bullets.index(b))
        for a in asteroids:
            a.x += a.xv
            a.y += a.yv
            if (a.x >= player.x - player.w//2 and a.x <= player.x + player.w//2) or a.x + a.w >= player.x - player.w//2 and a.x + a.w <= player.x + player.w//2:
                if (a.y >= player.y - player.h//2 and a.y <= player.y + player.h//2) or a.y + a.h >= player.y - player.h//2 and a.y + a.h <= player.y + player.h//2:
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    if isSoundOn:
                        bangLargeSound.play()
                    break
            for b in player_bullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x +b.w <= a.x +a.w:
                    if (b.y >= a.y and b.y <= a.y +a.h) or b.y >= b.h >= a.y and b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            if isSoundOn:
                                bangLargeSound.play()
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y =a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            if isSoundOn:
                                bangSmallSound.play()
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y =a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 30
                            if isSoundOn:
                                bangSmallSound.play()
                        asteroids.pop(asteroids.index(a))
                        player_bullets.pop(player_bullets.index(b))
                        break
        for s in stars:
            s.x += s.xv 
            s.y += s.yv
            if s.x < -100 - s.w or s.x > WIDTH + 100 or s.y > HEIGHT + 100 or s.y < -100 - s.h:
                stars.pop(stars.index(s))
                break
            for b in player_bullets:
                if (b.x >= s.x and b.x <= s.x + s.w) or b.x + b.w >= s.x and b.x +b.w <= s.x +s.w:
                    if (b.y >= s.y and b.y <= s.y +s.h) or b.y + b.h >= s.y and b.y + b.h <= s.y + s.h:
                        rapidFire = True
                        rfStart = count
                        stars.pop(stars.index(s))
                        player_bullets.pop(player_bullets.index(b))
                        break
        if lives <= 0:
            GameOver = True
        if rfStart != -1:
            if count - rfStart > 500:
                rapidFire = False
                rfStart = -1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.forward()
        if keys[pygame.K_SPACE]:
            if rapidFire:
                player_bullets.append(Bullet())
                if isSoundOn:
                    shoot.play()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not GameOver:
                    if not rapidFire:
                        player_bullets.append(Bullet())
                        if isSoundOn:
                            shoot.play()
            if event.key == pygame.K_s:
                isSoundOn = not isSoundOn
            if event.key == pygame.K_TAB:
                if GameOver:
                    GameOver = False
                    lives = 3
                    asteroids.clear()
                    aliens.clear()
                    alien_bullets.clear()
                    stars.clear()
                    if score > highScore:
                        highScore = score
                    score = 0
        if event.type == pygame.QUIT:
            pygame.quit()
    Redraw_gamewindow()