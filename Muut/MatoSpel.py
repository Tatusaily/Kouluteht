import random
import pygame, sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(1, gridsize-1)
        self.y = random.randint(1, gridsize-1)
        self.pos = Vector2(self.x, self.y)
        self.realpos = (self.pos.x * blocksize, self.pos.y * blocksize)

    def draw_fruit(self):
        pygame.draw.circle(playsurface, ("White"), self.realpos, blocksize/2.5)
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * gridsize, block.y * gridsize, blocksize, blocksize)
            pygame.draw.rect(playsurface, ("Green"), body_rect)

    def movesnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + directuib)


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

#GAMELOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(hudsurface, (0, 0))
    screen.blit(playsurface, (0, hudheight))
    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()
    pygame.time.Clock().tick(tickrate)