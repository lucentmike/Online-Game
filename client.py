import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x,self.y,self.width,self.height)




def reDrawWindow(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main(): 
    run = True
    p = Player(x = 50, y = 50, width = 100, height = 100, color = (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        reDrawWindow(win, p)

main()
