# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()

# alustetaan 640x480 ruutu
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

# ladataan pallon kuva
pallo = pygame.image.load("pallo.png")

# pallon koko ja liikkumisnopeus
pallo_x = randint(0, leveys)
pallo_y = randint(0, korkeus)
nopeus_x = 3
nopeus_y = 3

# kello
kello = pygame.time.Clock()

# silmukka
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    # maalataan ruutu mustaksi
    # lisataan pallo
    naytto.fill((0,0,0))
    naytto.blit(pallo, (pallo_x, pallo_y))
    pygame.display.flip()

    pallo_x += nopeus_x
    pallo_y += nopeus_y

    # suunnanvaihdot
    if pallo_x <= 0 or pallo_x + pallo.get_width() >= leveys:
        nopeus_x =- nopeus_x
    if pallo_y <= 0 or pallo_y + pallo.get_height() >= korkeus:
        nopeus_y =- nopeus_y

    kello.tick(60)