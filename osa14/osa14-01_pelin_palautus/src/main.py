import pygame
import time
from random import randint

class KolikkoSade:

    def __init__(self):
        pygame.init()

        self.lataa_kuvat()

        # Pelaajan sijainti
        self.pelaaja_x = 140
        self.pelaaja_y = 390

        # Naytto
        nayton_leveys = 320
        nayton_korkeus = 520
        self.naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus))

        self.fontti = pygame.font.SysFont("Arial", 16, True)

        pygame.display.set_caption("Kolikkosade")
        
        # Putoava esine
        self.putoavat_esineet = []
        self.nopeus = 1.0
        self.pisteet = 0

        self.uusi_peli()
        self.silmukka()

    # Lataa ja sailoo pelissa kaytettavat kuvat
    def lataa_kuvat(self):
        self.kuvat = []
        for nimi in ["robo", "kolikko"]:
            self.kuvat.append(pygame.image.load(nimi + ".png"))
        
        self.robo = self.kuvat[0]
        self.kolikko = self.kuvat[1]

    # Tarkastelee pelissa tapahtuvia muutoksia ja suorittaa muutokset
    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto(self)
            

    # Tarkasteee pelissa tapahtuvia muutoksia
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            # Pelin sulkeminen
            if tapahtuma.type == pygame.QUIT:
                exit()
            # Pelaajan liike
            elif tapahtuma.type == pygame.KEYDOWN:
                # Alusta uusi peli
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()
                # Sulkee pelin
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
                # Vasen nuolinappain
                if tapahtuma.key == pygame.K_LEFT:
                    self.pelaaja_x -= 10
                    # vasen raja
                    if self.pelaaja_x < 0:
                        self.pelaaja_x = 0
                # Vasen nuolinappain
                elif tapahtuma.key == pygame.K_RIGHT:
                    self.pelaaja_x += 10
                    # oikea raja
                    if self.pelaaja_x > 270:
                        self.pelaaja_x = 270
    
    # Piirtaa nayton
    def piirra_naytto(self, putoavat_esineet: list):
        self.naytto.fill((255, 153, 51))
        
        # Häviämisteksit
        if self.peli_loppu():
            teksti = self.fontti.render(f"Hävisit pelin! Pisteesi: {self.pisteet}", True, (255, 0, 0))
            teksti_x = 70
            teksti_y = 260
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))

        # Piirtaa pelaajan
        self.naytto.blit(self.robo, (self.pelaaja_x, self.pelaaja_y))
        #pygame.draw.rect(self.naytto, (255,0,0), self.hitbox,2)

        # Piirtaa pelin sisaiset ohjeet
        alusta = self.fontti.render("F2 = uusi peli ", True, (255, 255, 255))
        self.naytto.blit(alusta, (0, 500))
        poistu = self.fontti.render("| Esc = sulje peli ", True, (255, 255, 255))
        self.naytto.blit(poistu, (105, 500))

        # Piirtaa tippumisnopeus, piste ja elama tekstit
        tippumisnopeus = self.fontti.render("Tippumisnopeus: " + str("{0:.2f}".format(self.nopeus)), True, (255, 255, 255))
        self.naytto.blit(tippumisnopeus, (0, 0))
        pisteet = self.fontti.render("Pisteet: " + str(self.pisteet), True, (255, 255, 255))
        self.naytto.blit(pisteet, (0, 480))
        elamat = self.fontti.render("Elamat: " + str(self.elamat), True, (175, 0, 0))
        self.naytto.blit(elamat, (240, 480))

        # Piirtaa viivan esittamaan lattiaa
        viiva = pygame.draw.line(self.naytto, (255, 255, 255), (0, 475), (320, 475))
        
        # Pelaajan hitbox
        self.hitbox = (self.pelaaja_x, self.pelaaja_y, 50, 86)

        # Putoavan esineen logiikka
        for x, y in self.putoavat_esineet:
            if y > self.hitbox[1] and y > self.hitbox[1]:
                if x > self.hitbox[0] and x < self.hitbox[0] + self.hitbox[2]:
                    del self.putoavat_esineet[self.putoavat_esineet.index((x, y))]
                    self.lisaa_piste()
            if y > 490 or 0 < x > 290:
                del self.putoavat_esineet[self.putoavat_esineet.index((x, y))]
                if y > 490:
                    self.vahenna_elama()
            else:
                self.naytto.blit(self.kolikko, (x, y))

        for i, (x, y) in enumerate(self.putoavat_esineet):
            self.putoavat_esineet[i] = (x, y + self.nopeus)  # Paivita putoavan esineen sijainti y-akselilla
        
        self.lisaa_putoava_esine()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Luo putoavan esineen sattunaiseen kohtaan x-akselilla
    def lisaa_putoava_esine(self):
        x = randint(0, 320)
        y = 0

        if len(self.putoavat_esineet) < 1:
            self.putoavat_esineet.append((x, y))
        elif len(self.putoavat_esineet) > 1:
            self.putoavat_esineet.pop(0)

    # Alustaa pisteet, elamat ja pelaajan sijainnin
    def uusi_peli(self):
        self.pelaaja_x = 140
        self.pelaaja_y = 390
        self.elamat = 3
        self.pisteet = 0
        self.nopeus = 1.0

    # Lisaa pisteen ja tarkistaa lisataanko vaikeusastetta
    def lisaa_piste(self):
        self.pisteet += 1
        if self.pisteet % 2 == 0:
                self.nopeus += 0.2
    
    # Vahentaa pelaajalta elaman
    def vahenna_elama(self):
        self.elamat -= 1
        if self.elamat == 0:
            self.peli_loppu()
    
    # Tarkistaa pelin loppumisen
    def peli_loppu(self):
        if self.elamat == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    KolikkoSade()