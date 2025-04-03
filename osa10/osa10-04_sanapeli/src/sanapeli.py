import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # Verrataan pelaajien syottamien sanojen pituuksia
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            # P1 pidempi
            return 1
        elif len(pelaaja2_sana) > len(pelaaja1_sana):
            # P2 pidempi
            return 2
        else:
            # Tasapeli
            pass

class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    # Lasketaan vokaalit muodostamalla uusi sana [aeiouyäöå]
    def laske_vokaalit(self, syotto):
        vokaalit = ['a','e','i','o','u','y','ä','ö','å']
        sana = ""

        # Kaydaan syoton kirjaimet lapi
        for kirjain in syotto:
            # Jos vokaali niin lisataan se sanaan
            if kirjain in vokaalit:
                sana += kirjain
        # Muodostetaan uusi sana ja palautetaan se
        return sana

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # Verrataan pelaajien syottamien sanojen pituuksia
        if len(self.laske_vokaalit(pelaaja1_sana)) > len(self.laske_vokaalit(pelaaja2_sana)):
            # P1 pidempi
            return 1
        elif len(self.laske_vokaalit(pelaaja2_sana)) > len(self.laske_vokaalit(pelaaja1_sana)):
            # P2 pidempi
            return 2
        else:
            # Tasapeli
            pass

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # Tarkistetaan onko sana
        if pelaaja1_sana not in ["kivi","paperi","sakset"]:
            if pelaaja2_sana not in ["kivi","paperi","sakset"]:
                return
            else:
                return 2
        elif pelaaja2_sana not in ["kivi","paperi","sakset"]:
            return 1

        # Tarkistetaan mahdollisuudet
        if pelaaja1_sana == pelaaja2_sana:
            pass
        elif pelaaja1_sana == "kivi":
            if pelaaja2_sana == "sakset":
                return 1
            elif pelaaja2_sana == "paperi":
                return 2
        elif pelaaja1_sana == "sakset":
            if pelaaja2_sana == "paperi":
                return 1
            elif pelaaja2_sana == "kivi":
                return 2
        elif pelaaja1_sana == "paperi":
            if pelaaja2_sana == "kivi":
                return 1
            elif pelaaja2_sana == "sakset":
                return 2
    

if __name__ == '__main__':
    #p = Sanapeli(3)
    #p.pelaa()
    #p = PisinSana(3)
    #p.pelaa()
    #p = EnitenVokaaleja(4)
    #p.pelaa()
    p = KiviPaperiSakset(4)
    p.pelaa()