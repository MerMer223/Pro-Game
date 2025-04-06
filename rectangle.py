import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
class Rectangle():
    def __init__(self,color,pos,length,width):
        self.color = color
        self.pos = pos
        self.length = length
        self.width = width
        self.rect = screen
    def draw(self,):
        self.Draw_rect = pygame.draw.rect(self.rect,self.color,self.pos,self.length,self.width)
    def grow(self,l,w):
        self.length = self.length+l
        self.width = self.width+w
        self.Draw_rect = pygame.draw.rect(self.rect,self.color,self.pos,self.length,self.width)
Rect1 = Rectangle("Green",(400,400),50,100)
Rect2 = Rectangle("Blue",(400,600,),20,200)
Rect3 = Rectangle("Red",(600,400),75,400)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            Rect1.draw()
            Rect2.draw()
            Rect3.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            Rect1.grow(50,50)
            Rect2.grow(20,20)
            Rect3.grow(75,20)
            pygame.display.update()
        elif(event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            Rect4 = Rectangle("Black",(pos),100,500)
            Rect4.draw()
            pygame.display.update()