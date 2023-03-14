import pygame
import sys
from pygame.math import Vector2
pygame.init()

gridsize = 20
charfont = pygame.font.SysFont("Arial", gridsize)


class PlayerChar:
    x = 150
    y = 150
    speed = gridsize

    def __init__(self):
        self.glyph = charfont.render("@", False, "Green")
        self.rect = self.glyph.get_rect(center=(self.x, self.y))

    def move(self, direction):
        if direction == "right":
            self.x = self.x + self.speed
            self.rect.move_ip(self.speed, 0)
        elif direction == "left":
            self.x = self.x - self.speed
            self.rect.move_ip(-self.speed, 0)
        elif direction == "up":
            self.y = self.y - self.speed
            self.rect.move_ip(0, -self.speed)
        elif direction == "down":
            self.y = self.y + self.speed
            self.rect.move_ip(0, self.speed)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * gridsize, block.y * gridsize, blocksize, blocksize)
            pygame.draw.rect(playsurface, "Green", body_rect)

    def movesnake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


def input_tick():
    print(f"{Player.x}, {Player.y}")


# Game On
if __name__ == '__main__':
    screen = pygame.display.set_mode((600, 600))
    print("Main")
    Player = PlayerChar()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # input
                if event.key == pygame.K_UP:
                    Player.move("up")
                if event.key == pygame.K_DOWN:
                    Player.move("down")
                if event.key == pygame.K_LEFT:
                    Player.move("left")
                if event.key == pygame.K_RIGHT:
                    Player.move("right")
                input_tick()

        screen.fill("Black")
        screen.blit(Player.glyph, Player.rect)
        pygame.display.update()
        pygame.time.Clock().tick(30)
