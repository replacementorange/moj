import pygame

pygame.init()

# Puolitetaan nayton koko nopeuttaakseen debuggaamista
#naytto_leveys = 320
#naytto_korkeus = 240
naytto_leveys = 640
naytto_korkeus = 480
naytto = pygame.display.set_mode((naytto_leveys, naytto_korkeus))

robo = pygame.image.load("robo.png")

# Robo leveys ja korkeus
leveys = robo.get_width()
korkeus = robo.get_height()

x = 0
y = 0
nopeus = 1

# Kaytetaan suuntanumeroa ohjamaan logiikkaa
suunta = 1 # 1 o, 2 a, 3 v, 4 y

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    
    # Toimintalogiikka:
    if suunta == 1: # oikea
        x += nopeus
        # Tarkistus, etta missa mennaan
        if x + leveys == naytto_leveys:
            suunta = 2
    elif suunta == 2: # alas
        y += nopeus
        if y + korkeus == naytto_korkeus:
            suunta = 3
    elif suunta == 3: # vasen
        x -= nopeus
        if x == 0:
            suunta = 4
    elif suunta == 4: # ylos
        y -= nopeus
        if y == 0:
            suunta = 1

    kello.tick(60)