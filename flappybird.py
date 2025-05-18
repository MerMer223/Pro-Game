import pygame
import random
from pygame.locals import *
pygame.init()
WIDTH = 800
HEIGHT = 800
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
fps = 60
ground_scroll = 0
scroll_speed = 4
bg = pygame.image.load("Pygame/images/fbbackground.png")
ground = pygame.image.load("Pygame/images/fbground.png")
restart = pygame.image.load("Pygame/images/fbrestart.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
flying = False
Gameover = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
font = pygame.font.SysFont('Bauhause93',60)
white = 255,255,255
score = 0
pass_pipe = False
def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(HEIGHT / 2) 
    score = 0 
    return score
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))
class Button():
    def __init__ (self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action
class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pygame/images/fbpillar.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - int(pipe_gap / 2)]
        if pos == - 1:
            self.rect.topleft = [x,y + int(pipe_gap / 2)]
    def update(self):
        self.rect.x -= scroll_speed 
        if self.rect.right <0:
            self.kill()
class Bird(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"Pygame/images/fb{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.click = False
    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)
        if Gameover == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            self.counter += 1
            flap_cooldown = 5
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images [self.index]
            self.image = pygame.transform.rotate(self.images[self.index],self.velocity*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100,int(HEIGHT/2))
button = Button(WIDTH // 2 - 50 , HEIGHT // 2 - 100, restart)
bird_group.add(flappy)
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(ground_scroll,700))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    bird_group.update()
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
        and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
        and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    draw_text(str(score),font,white,int(WIDTH / 2), 20)
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top <0:
        Gameover = True
    if flappy.rect.bottom > 768:
        Gameover = True
        flying = False
    if Gameover == False and flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height , -1)
            top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height , 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()
    if Gameover == True:
        if button.draw() == True:
            Gameover = False
            score = reset_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and Gameover == False:
            flying = True
    pygame.display.update()