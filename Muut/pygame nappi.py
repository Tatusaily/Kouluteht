#Tässä harjoitellaan napin tekemistä pygamella
import pygame
import sys
pygame.init()

#Vakiot
menufont = pygame.font.SysFont("Arial", 24, True)
screenx = 800
screeny = 600
screen = pygame.display.set_mode((screenx, screeny))

class MENUBUTTON(txt, x, y):
    #Nappi jossa on tekstiä
    #Nappi haluaa tekstin ja sijainnin
    def __init__(self, txt, x, y):
        text = menufont.render(self.txt, True, "WHITE")

    def draw(self, x, y):
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    MENUBUTTON.__init__("Moi", )
    pygame.display.update()