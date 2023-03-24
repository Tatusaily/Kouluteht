# Game On
import random
import pygame
import sys
from pygame import Vector2
from Muut.Hymyprint import hymyprint as hymy

if __name__ == '__main__':
    # Vakiot ja bloat
    pygame.init()
    gridsize = 40
    grid_width = 10
    grid_heigth = 10
    window_width = grid_width*gridsize
    window_height = grid_heigth*gridsize
    screen = pygame.display.set_mode((window_width, window_height))
    gameclock = pygame.time.Clock()
    charfont = pygame.font.SysFont("Gotham", gridsize)

    class PlayerChar:
        def __init__(self):
            self.x = 1*gridsize/2
            self.y = 1*gridsize/2
            self.pos = Vector2(self.x, self.y)
            self.speed = gridsize
            # .render tekee uuden surfacen. sen voi blittaa mihin haluu
            self.glyph = charfont.render("@", True, "Green")
            self.rect = self.glyph.get_rect(center=(self.x, self.y))

        def move(self, direction):
            if direction == "right":
                self.x = self.x + self.speed
            elif direction == "left":
                self.x = self.x - self.speed
            elif direction == "up":
                self.y = self.y - self.speed
            elif direction == "down":
                self.y = self.y + self.speed

            # Rajoitetaan self koordinaatit ruudukkoon:
            if self.x <= 0:
                self.x = gridsize/2
            if self.x > window_width:
                self.x = window_width - gridsize/2
            if self.y <= 0:
                self.y = gridsize/2
            if self.y > window_height:
                self.y = window_height - gridsize/2

            # Päivitetään rect oikeaan koordinaatiin
            self.rect = self.glyph.get_rect(center=(self.x, self.y))
            self.pos = Vector2(self.x, self.y)

    class Snake:
        # TODO: Mato huijaa sääntöjä ja liikkuu diagonaalisesti eikä välitä ruuduista
        def __init__(self, length=3):
            self.body = []
            self.speed = gridsize
            self.direction = Vector2(0, 0)
            self.pos = (random.randint(0, grid_width)*gridsize, random.randint(0, grid_heigth)*gridsize)
            for i in range(length):
                self.body.append(Vector2(self.pos))
            while self.direction[0] == 0 or self.direction[1] == 0:
                self.direction = Vector2(random.randint(-1, 1), random.randint(-1, 1))

        def turn(self):
            # RNG
            if random.randint(0, 1) == 1:
                # Jos liike on sivuttasta; käännetään mato joko ylös tai alas.
                if self.direction[0] == 1 or self.direction[0] == -1:
                    self.direction[0] = 0
                    while self.direction[1] == 0:
                        self.direction[1] = random.randint(-1, 1)
                # Jos liike on pystysuuntaista; käännetään matoa vasemmalle tai oikealle.
                if self.direction[1] == 0 or self.direction[1] == -1:
                    self.direction[1] = 0
                    while self.direction[0] == 0:
                        self.direction[0] = random.randint(-1, 1)


        def move(self):
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction*self.speed)
            self.body = body_copy[:]

            if self.body[0][0] <= 0:
                self.body[0][0] = gridsize/2
            if self.body[0][0] > window_width:
                self.body[0][0] = window_width - gridsize/2
            if self.body[0][1] <= 0:
                self.body[0][1] = gridsize/2
            if self.body[0][1] > window_height:
                self.body[0][1] = window_height - gridsize/2

        def draw_snake(self):
            for block in self.body:
                body_rect = pygame.Rect(block.x, block.y, gridsize, gridsize)
                pygame.draw.rect(screen, "Red", body_rect)


    def input_tick():
        print(f"{int(Player.x/gridsize+1)}, {int(Player.y/gridsize+1)}")

    def draw_grid():
        for x in range(0, window_width, gridsize):
            for y in range(0, window_height, gridsize):
                rect = pygame.Rect(x, y, gridsize, gridsize)
                pygame.draw.rect(screen, (150, 150, 150), rect, 1)

    print("Main")
    Player = PlayerChar()
    Sneikki = Snake()
    testblock = pygame.Rect((4*gridsize, 4*gridsize), (gridsize, gridsize))
    hymy()
    snake_act = pygame.USEREVENT
    pygame.time.set_timer(snake_act, 1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                pygame.quit()
                sys.exit()
            if event.type == snake_act:
                print(f"Sneikki: {Sneikki.body}")
                print(f"Playa: {Player.pos}")
                Sneikki.move()
                Sneikki.turn()
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
        if Player.rect.colliderect(testblock):
            print("KOSKEE")
            Player = PlayerChar()

        # Draw UI

        screen.fill("Black")
        screen.blit(Player.glyph, Player.rect)
        pygame.draw.rect(screen, "White", testblock)
        draw_grid()
        Sneikki.draw_snake()

        pygame.display.update()
