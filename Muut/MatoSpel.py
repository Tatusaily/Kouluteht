import random
import pygame, sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(1, gridsize-1)
        self.y = random.randint(1, gridsize-1)
        self.pos = Vector2(self.x, self.y)
        self.realpos = (self.pos.x * blocksize - blocksize/2, self.pos.y * blocksize - blocksize/2)

    def draw_fruit(self):
        pygame.draw.circle(playsurface, ("White"), self.realpos, blocksize/2.5)
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * gridsize, block.y * gridsize, blocksize, blocksize)
            pygame.draw.rect(playsurface, ("Green"), body_rect)

    def movesnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


#VAKIOT
pygame.init()
gridsize = 20
blocksize = 40
hudheight = 40
screen = pygame.display.set_mode((gridsize*blocksize, gridsize*blocksize+hudheight))
playsurface = pygame.Surface((gridsize*blocksize, gridsize*blocksize))
hudsurface = pygame.Surface((gridsize*blocksize, hudheight))
hudsurface.fill("Gray")
playsurface.fill("Black")
pygame.display.set_caption("Sneikki")
tickrate = 60

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 50) #Suorittaa SCREEN_UPDATEn joka 50ms

#GAMELOOP
while True:
    #Eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE: #pelinopeus
            snake.movesnake()
        if event.type == pygame.KEYDOWN: #input
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)

    #UI Piirto
    screen.blit(hudsurface, (0, 0))
    screen.blit(playsurface, (0, hudheight))
    hudsurface.fill("Gray")
    playsurface.fill("Black")

    #Mato ja hedelmä piirto
    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()
    pygame.time.Clock().tick(tickrate)