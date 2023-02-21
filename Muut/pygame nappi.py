#Tässä harjoitellaan napin tekemistä pygamella
import pygame
import sys
pygame.init()

#Vakiot
menufont = pygame.font.SysFont("Arial", 24, True)
screen = pygame.display.set_mode((800, 600))

class TXTBUTTON:
    #Nappi jossa on tekstiä
    #Nappi haluaa tekstin ja sijainnin
    def __init__(self, text, x, y):
        return


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()