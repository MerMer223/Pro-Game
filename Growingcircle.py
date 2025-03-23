import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
class Circle():
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.circle = screen
    def draw(self):
        self.Draw_circle = pygame.draw.circle(self.circle,self.color,self.pos,self.radius,self.width)
    def grow(self,r):
        self.radius = self.radius+r
        self.Draw_circle = pygame.draw.circle(self.circle,self.color,self.pos,self.radius,self.width)
Ball1 = Circle("Green",(400,400),50,100)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            Ball1.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            Ball1.grow(50)
            pygame.display.update()
