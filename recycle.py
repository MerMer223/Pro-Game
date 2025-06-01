import pygame
import random
import time
from pygame.locals import *
pygame.init()
WIDTH = 800
HEIGHT = 800
RECYCLE_SOUND = pygame.mixer.Sound("Pygame/images/recyclebin-102273.mp3")
PLASTIC_SOUND = pygame.mixer.Sound("Pygame/images/broken-beer-bottle-311131.mp3")
white = (255,255,255)
red = (255,0,0)
score = 0
clock = pygame.time.Clock()
starttime = time.time()
myFont = pygame.font.SysFont("Times New Roman",22)
timingFont = pygame.font.SysFont("Times New Roman",22)
text = myFont.render("Score =" +str(0),True,white)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
def changebackground(img):
    image = pygame.image.load(img)
    bg = pygame.transform.scale(image,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/images/bin.png")
      #  self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
class Recycle(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
       # self.image = pygame.transform.scale(self.image,(400,400))
        self.rect = self.image.get_rect()
class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/images/plasticbag.png")
        #self.image = pygame.transform.scale(self.image,(400,400))
        self.rect = self.image.get_rect()
images = ["Pygame/images/paperbag.png","Pygame/images/woodcrate.png","Pygame/images/pencil.png"]
itemlist = pygame.sprite.Group()
allsprite = pygame.sprite.Group()
plasticlist = pygame.sprite.Group()
for i in range(50):
    item = Recycle(random.choice(images))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    itemlist.add(item)
    allsprite.add(item)
for i in range(20):
    plastic = Nonrecycle()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plasticlist.add(plastic)
    allsprite.add(plastic)

bin = Bin()
allsprite.add(bin)

run = True
while run:
    clock.tick(30)
    timeElapsed = time.time()-starttime
    if timeElapsed >= 60:
        if score > 50:
            text = myFont.render("bin loot successful",True,red)
            changebackground("Pygame/images/gameover.jpg")
        else:
            text = myFont.render("better luck next time",True,red)
            changebackground("Pygame/images/youlose.jpg")
        screen.blit(text,(300,400))
    else:
        changebackground("Pygame/images/reusable.png")
        countdown = timingFont.render("time left"+str(60-int(timeElapsed)),True,red)
        screen.blit(countdown,(700,50))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 800:
                bin.rect.y += 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 800:
                bin.rect.x += 5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        item_hit_list = pygame.sprite.spritecollide(bin,itemlist,True)
        plastic_hit_list = pygame.sprite.spritecollide(bin,plasticlist,True)
        for i in item_hit_list:
            score += 1
            RECYCLE_SOUND.play()
            text = myFont.render("score ="+str(score),True,red)
        for i in plastic_hit_list:
            score -= 5
            PLASTIC_SOUND.play()
            text = myFont.render("score ="+str(score),True,red)
        screen.blit(text,(700,100))
        allsprite.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()