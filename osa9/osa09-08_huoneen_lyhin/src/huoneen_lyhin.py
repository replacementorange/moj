# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi
    
class Huone():
    def __init__(self):
        self.henkilot = []
    
    def lisaa(self, henkilo: Henkilo):
        self.henkilot.append(henkilo)

    def on_tyhja(self):
        if len(self.henkilot) == 0:
            return True
        else:
            return False

    def tulosta_tiedot(self):
        for henkilo in self.henkilot:
            print(f"{henkilo} ({henkilo.pituus} cm)")

    def lyhin(self):
        if self.on_tyhja():
            return None
        henkilo = sorted([(henkilo.pituus, henkilo) for henkilo in self.henkilot])
        #print(henkilo)
        return henkilo[0][1]
    
    def poista_lyhin(self):
        if self.on_tyhja():
            return None
        
        lyhin = self.lyhin()
        if lyhin:
            self.henkilot.remove(lyhin)
        
        return lyhin

if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()