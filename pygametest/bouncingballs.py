import sys, pygame
import random

pygame.init()
random.seed()

windowsize = windowwidth, windowheight = 640, 480
black = 0, 0, 0
screen = pygame.display.set_mode(windowsize)

class Ball:
    imagetemplate = pygame.image.load("pygametest\\intro_ball.gif")
    imagerect = imagetemplate.get_rect()
    Clock = pygame.time.Clock()
    
    def __init__(self):
        pos = (random.randint(1, windowwidth - Ball.imagerect.width - 10), 0)
        r = int(random.randint(- int(windowwidth / 10), int(windowwidth / 10)) )
        br = Ball.imagerect.inflate(r, r)
        self._image = pygame.transform.scale(Ball.imagetemplate, (br.width, br.height))
        self._ballrect = pygame.Rect(pos[0], pos[1], br.width, br.height)
        self._InterMoveWaitTime = random.randint(1, 20)
        self._direction = [1, 1]
        self._TotalWaitSinceLastMove = 0

    def move(self):
        self._TotalWaitSinceLastMove = self._TotalWaitSinceLastMove + Ball.Clock.get_time()
        if self._TotalWaitSinceLastMove <= self._InterMoveWaitTime:
            return

        self._TotalWaitSinceLastMove = 0

        self._ballrect = self._ballrect.move(self._direction)
        if self._ballrect.left < 0 or self._ballrect.right > windowwidth:
            self._direction[0] = -self._direction[0]
        if self._ballrect.top < 0 or self._ballrect.bottom > windowheight:
            self._direction[1] = -self._direction[1]

    def speeddown(self):
        self._InterMoveWaitTime = self._InterMoveWaitTime + 1

    def speedup(self):
        self._InterMoveWaitTime = self._InterMoveWaitTime - 1

    def draw(self, screen):
        screen.blit(self._image, self._ballrect)
       
balls = [Ball() for i in range(4)]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for b in balls:
                    b.speeddown()
            elif event.key == pygame.K_UP:
                for b in balls:
                    b.speedup()
 
    screen.fill(black)   
    for b in balls:
        b.move()
        b.draw(screen)
    pygame.display.flip()

    Ball.Clock.tick()