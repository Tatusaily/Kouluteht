#Tässä harjoitellaan napin tekemistä pygamella
import pygame
import sys
pygame.init()

#Vakiot
menufont = pygame.font.SysFont("Comic Sans", 35, True)
screenx = 800
screeny = 600
screen = pygame.display.set_mode((screenx, screeny))

class MENUBUTTON:
    #Nappi jossa on tekstiä
    #Nappi haluaa tekstin ja sijainnin
    def __init__(self, txt, x, y):
        text = menufont.render(txt, True, "WHITE")

    def draw(self, x, y):
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    text = menufont.render("MOI!", True, "WHITE")
    text_rect = text.get_rect(center=(screenx/2, screeny/3))
    screen.blit(text, text_rect)

    pygame.display.update()