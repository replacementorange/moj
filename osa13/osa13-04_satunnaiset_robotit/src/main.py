# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))

leveys = robo.get_width()
korkeus = robo.get_height()

# arvotaan sattunaiset koordinaatit 1000 kertaa
for i in range(1000):
    x = randint(0, 640 - leveys)
    y = randint(0, 480 - korkeus)
    naytto.blit(robo, (x, y))

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()