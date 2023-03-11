import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill("Black")
    print("Main")

    while True:
        pygame.display.update()

