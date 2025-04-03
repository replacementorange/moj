# Tee ratkaisusi tähän:

# Tavara luokka, josta muodostetut oliot vastaavat erilaisia tavaroita
class Tavara:

    # Konstruktor
    def __init__(self, nimi: str, paino: int):
        self.n = nimi
        self.p = paino

    # Palauta tavaran nimi
    def nimi(self):
        return self.n

    # Palauta tavaran paino
    def paino(self):
        return self.p

    # Palauta merkkijono tavaran nimesta ja painosta (kg)
    def __str__(self):
        return f"{self.n} ({self.p} kg)"

# Matkalaukku luokka, joka maarittelee suurimman mahdollisen yhteinspainon
class Matkalaukku:

    # Konstruktori
    def __init__(self, maksimipaino: int):
        self.tavarat = []
        self.maksimipaino = maksimipaino

    # Lisaa tavara jos maksimipaino ei ylity
    def lisaa_tavara(self, tavara: Tavara):
        if self.paino() + tavara.paino() <= self.maksimipaino:
            self.tavarat.append(tavara)

    # Tulosta sisalla olevat tavarat
    def tulosta_tavarat(self):
        for t in self.tavarat:
            print(t)

    # Laskee yhteispainon
    def paino(self):
        yhteensa = 0
        for t in self.tavarat:
            yhteensa += t.paino()
        return yhteensa

    # Etsii painavimman esineen
    def raskain_tavara(self):
        s = sorted(self.tavarat, key=lambda t: t.paino())
        return s[-1]
    
    # Palauttaa kielihuolletun merkkijonon
    def __str__(self):
        if len(self.tavarat) == 0:
            return f"0 tavaraa ({self.paino()} kg)"
        
        elif len(self.tavarat) == 1:
            return f"1 tavara ({self.paino()} kg)"
        
        else:
            return f"{len(self.tavarat)} tavaraa ({self.paino()} kg)"

# Lastiruuma luokka, joka valvoo, etta matkalaukkujen yhteispaino ei ylita maksimipainoa
class Lastiruuma:

    # Konstruktori
    def __init__(self, maksimipaino: int):
        self.matkalaukut = []
        self.maksimipaino = maksimipaino

    # Laskee painon
    def paino(self):
        yht = 0
        for m in self.matkalaukut:
            yht += m.paino()
        return yht
    
    # Lisaa matkalaukun
    def lisaa_matkalaukku(self, laukku):
        if self.paino() + laukku.paino() <= self.maksimipaino:
            self.matkalaukut.append(laukku)

    # Tulostaa tavarat
    def tulosta_tavarat(self):
        for m in self.matkalaukut:
            for t in m.tavarat:
                print(t)

    # Palauttaa merkkijonot
    def __str__(self):
        tilaa = self.maksimipaino - self.paino()
        if len(self.matkalaukut) == 0:
            return f"0 matkalaukkua, tilaa {tilaa} kg"
        
        elif len(self.matkalaukut) == 1:
            return f"1 matkalaukku, tilaa {tilaa} kg"
        
        else:
            return f"{len(self.matkalaukut)} matkalaukkua, tilaa {tilaa} kg"


if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()