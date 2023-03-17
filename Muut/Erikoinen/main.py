

# Game On
if __name__ == '__main__':
    import pygame
    import sys
    from pygame import Vector2
    from Muut.Hymyprint import hymyprint as hymy
    # Vakiot ja bloat
    pygame.init()
    gridsize = 40
    window_width = gridsize*10
    window_height = gridsize*10
    screen = pygame.display.set_mode((window_width, window_height))
    gameclock = pygame.time.Clock()
    charfont = pygame.font.SysFont("Gotham", gridsize)

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

    class Snake:
        def __init__(self, length):
            self.body = []
            # TODO: Kärmeelle kehonrakennus.
            #   Käärmeelle tulee kehoon satunnainen määrä paloja. Myöhemmin enemmän?
            #   Kaikki palat tulee samaan kohtaan:
            #       Kun käärme lähtee liikkeelle niin se ikäänkuin kasvaa siitä pisteestä.
            #   Sit käärmeelle suunta ja nopeus
            #   Käärme vois alkuun liikkuu satunnaisiin suuntiin.
            #       Myöhemmin etsii pelaajaa?

            #for i in length:
                #self.body.append(Vector2(x, y))

    def input_tick():
        print(f"{int(Player.x/gridsize+1)}, {int(Player.y/gridsize+1)}")

    def draw_grid():
        for x in range(0, window_width, gridsize):
            for y in range(0, window_height, gridsize):
                rect = pygame.Rect(x, y, gridsize, gridsize)
                pygame.draw.rect(screen, (150, 150, 150), rect, 1)

    print("Main")
    Player = PlayerChar()
    testblock = pygame.Rect((4*gridsize, 4*gridsize), (gridsize, gridsize))
    hymy()
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
        if Player.rect.colliderect(testblock):
            print("KOSKEE")
            Player = PlayerChar()

        # Draw UI
        screen.fill("Black")
        screen.blit(Player.glyph, Player.rect)
        pygame.draw.rect(screen, "White", testblock)
        draw_grid()

        pygame.display.update()
