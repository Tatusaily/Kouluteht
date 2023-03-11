import pygame
import sys


class PlayerChar:
    x = 10
    y = 10
    speed = 1

    def move(self, direction):
        if direction == "right":
            self.x = self.x + self.speed
        elif direction == "left":
            self.x = self.x - self.speed
        elif direction == "up":
            self.y = self.y - self.speed
        elif direction == "down":
            self.y = self.y + self.speed


def input_tick():
    print(f"{Player.x}, {Player.y}")


# Game On
Player = PlayerChar()
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    print("Main")

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

        pygame.display.update()
        pygame.time.Clock().tick(30)
