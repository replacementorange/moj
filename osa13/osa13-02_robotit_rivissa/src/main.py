# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))

# Haetaan robolle leveys
leveys = robo.get_width()

#naytto.blit(robo, (100, 50))
# Piirretaan 10 robottia for silmukalla
for robotti in range(0, 10):
    # Piirretaan robotit 50px etaisyydella toisistaan, korkeudelle 50
    naytto.blit(robo, (50 + leveys * robotti, 50))
    
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()