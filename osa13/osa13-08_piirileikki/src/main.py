# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

leveys = robo.get_width()

kulma = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))

    # naytto.blit(robo, (x, y))
    # https://fi.wikipedia.org/wiki/Ympyr%C3%A4 {\displaystyle p=2\pi r\ }, jossa r {\displaystyle r} on ympyrän säde ja π   {\displaystyle \pi \ \,}on vakio pii noin 3,14.
    luku = 10 # --> + 2 * math.pi * robotti / luku
    for robotti in range(luku): 
        x = 320 + math.cos(kulma + 2 * math.pi * robotti / luku) * 150 - robo.get_width() / 2
        y = 240 + math.sin(kulma + 2 * math.pi * robotti / luku) * 150 - robo.get_height() / 2
        naytto.blit(robo, (x, y))
        
    pygame.display.flip()

    kulma += 0.01
    kello.tick(60)