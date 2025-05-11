import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/images/rocketship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
    def update(self,pressedkeys):
        if pressedkeys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressedkeys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressedkeys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressedkeys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left <0:
            self.rect.left = 0
        elif self.rect.right >WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <=0:
            self.rect.top = 0
        elif self.rect.bottom >=HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()

def startgame(): 
    player = Player()

    sprites.add(player)

    while run:
        pressedkeys = pygame.key.get_pressed()
        player.update(pressedkeys)
        screen.blit(pygame.image.load("Pygame/images/space.png"),(0,0))
        sprites.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
startgame()