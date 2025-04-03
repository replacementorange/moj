# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
x2 = 0
y = 0
nopeus = 1
nopeus2 = 2
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    # Robo 1
    naytto.blit(robo, (x, y + 50))

    # Robo 2
    naytto.blit(robo, (x2, y + 200))
    pygame.display.flip()
    
    x += nopeus
    if nopeus > 0 and x+robo.get_width() >= 640:
        nopeus = -nopeus
    if nopeus < 0 and x <= 0:
        nopeus = -nopeus

    x2 += nopeus2
    if nopeus2 > 0 and x2+robo.get_width() >= 640:
        nopeus2 = -nopeus2
    if nopeus2 < 0 and x2 <= 0:
        nopeus2 = -nopeus2

    kello.tick(60)