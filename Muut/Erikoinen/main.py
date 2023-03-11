import pygame
import sys

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
                    print("UP")
                if event.key == pygame.K_DOWN:
                    print("DOWN")
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")

        pygame.display.update()
        # pygame.time.Clock().tick(60)
