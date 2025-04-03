# Tämän osan tehtävissä ei ole automaattisia testejä, vaan testi antaa pisteet
# automaattisesti, kun lähetät ratkaisun palvelimelle. Lähetä ratkaisu vasta
# sitten, kun se on valmis ja vastaa tehtävänannon vaatimuksia. Vaikka tehtävissä
# ei ole testejä, kurssin henkilökunta näkee lähetetyt ratkaisut.

# TEE RATKAISUSI TÄHÄN:
import pygame
# Maaritellaan leveys ja korkeus omiksi
ruudun_leveys = 640
ruudun_korkeus = 480

pygame.init()
naytto = pygame.display.set_mode((ruudun_leveys, ruudun_korkeus))

# Robotin kuva
robo = pygame.image.load("robo.png")

# Haetaan robolle mitat
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0, 0, 0))

# Robotit
naytto.blit(robo, (0, 0)) # VYK
naytto.blit(robo, (ruudun_leveys - leveys, 0)) # VYK
naytto.blit(robo, (0, ruudun_korkeus - korkeus)) # VAK
naytto.blit(robo, (ruudun_leveys - leveys, ruudun_korkeus - korkeus)) # OAK
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
