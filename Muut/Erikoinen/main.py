import pygame
import sys

# Game On
if __name__ == '__main__':
    # Vakiot ja bloat
    pygame.init()
    window_width = 800
    window_height = 600
    gridsize = 40
    screen = pygame.display.set_mode((window_width, window_height))
    gameclock = pygame.time.Clock()
    charfont = pygame.font.SysFont("Arial", gridsize-5)

    class PlayerChar:
        speed = gridsize

        def __init__(self):
            self.x = 1*gridsize/2
            self.y = 1*gridsize/2
            # .render tekee uuden surfacen. sen voi blittaa mihin haluu
            self.glyph = charfont.render("@", True, "Green")
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

    def input_tick():
        print(f"{int(Player.x/gridsize)}, {int(Player.y/gridsize)}")

    def draw_grid():
        for x in range(0, window_width, gridsize):
            for y in range(0, window_height, gridsize):
                rect = pygame.Rect(x, y, gridsize, gridsize)
                pygame.draw.rect(screen, (150, 150, 150), rect, 1)

    print("Main")
    Player = PlayerChar()
    testblock = pygame.Rect((4*gridsize, 4*gridsize), (gridsize, gridsize))

    while True:
        if Player.rect.colliderect(testblock):
            print("KOSKEE")
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

        # Draw UI
        screen.fill("Black")
        screen.blit(Player.glyph, Player.rect)
        pygame.draw.rect(screen, "White", testblock)
        draw_grid()

        pygame.display.update()
