import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60
class Ball:
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = 200
        self.vy = 0
        self.gravity = 2000
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)
    def update(self,t):
        uy = self.vy #intial velocity
        self.vy += self.gravity * t #final velocity
        self.y += (uy + self.vy) * 0.5 * t
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy = -self.vy * 0.9
        self.x += self.vx * t
        if self.x > WIDTH - self.r or self.x < self.r:
            self.vx = - self.vx
Bob = Ball (75,75,75,"Green")
Brady = Ball (700,75,100,"red")
run = True
while run:
    t = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bob.vy = - 500
            if event.key == pygame.K_0:
                Brady.vy = - 500
        
    screen.fill("White")
    Bob.draw()
    Bob.update(t)
    Brady.draw()
    Brady.update(t)
    pygame.display.flip()