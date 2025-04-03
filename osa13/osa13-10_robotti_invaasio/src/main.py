# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()

# alustetaan 640x480 ruutu
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

# ladataan robon kuva
robo = pygame.image.load("robo.png")

# robon koko ja liikkumisnopeus
robo_x = 0
robo_y = 0 - robo.get_height()
nopeus = 2
robot = [] # taulukko robojen sailytykseen
#nopeus_y = 3

# kello
kello = pygame.time.Clock()

# silmukka
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    # luo robotin sattunaiseen koordinaattiin 1-100
    luo_robo = randint(1, 100)
    if luo_robo <= 2:
        robot.append([randint(0, leveys - robo.get_width()), robo_y])
        # tarkastellaan luotujen maaraa
        if len(robot) > 30:
            robot.pop(0)
    
    for robotti in robot:
        if robotti[1] + robo.get_height() < korkeus:
            robotti[1] += 1
        elif robotti[0] > leveys / 2:
            robotti[0] += 1
        else:
            robotti[0] -= -1
    
    # piirretaan naytolle
    naytto.fill((0,0,0))
    for robotti in robot:
        naytto.blit(robo, (robotti[0], robotti[1]))
    pygame.display.flip()

    kello.tick(60)