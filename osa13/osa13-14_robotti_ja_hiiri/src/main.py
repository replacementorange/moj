# TEE RATKAISUSI TÄHÄN:
import pygame

# alustukset
pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

# ladataan kuva
robo = pygame.image.load('robo.png')

# robon ja hiiren koord.
robo_x, robo_y = 0, 0
hiiri_x, hiiri_y = 0, 0

# silmukka
while True:
    for tapahtuma in pygame.event.get():
        # tarkistetaan onko hiiren liike
        if tapahtuma.type == pygame.MOUSEMOTION:

            # hiiren x ja y
            hiiri_x = tapahtuma.pos[0]-robo.get_width()/2
            hiiri_y = tapahtuma.pos[1]-robo.get_height()/2
            
            # robon x ja y
            robo_x = min(max(hiiri_x, 0), leveys - robo.get_width())
            robo_y = min(max(hiiri_y, 0), korkeus - robo.get_height())

            naytto.fill((0, 0, 0))
            naytto.blit(robo, (robo_x, robo_y))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit()
    
