# TEE RATKAISUSI TÄHÄN:
class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f'{self.nimi}, superkyvyt: {self.supervoimat}'

class SuperRyhma(SuperSankari):
    def __init__(self, nimi: str, kotipaikka: str):
        # Suojatut attribuutit
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []

    # Havainnointi metodit nimelle ja kotipaikalle
    @property
    def nimi(self):
        return self._nimi

    @property
    def kotipaikka(self):
        return self._kotipaikka

    # Metodi lisaa jasen
    def lisaa_jasen(self, sankari: SuperSankari):
        # Lisataan jasen listaan
        self._jasenet.append(sankari)

    # Metodi tulosta ryhma
    def tulosta_ryhma(self):
        # tulostetaan ryhman nimi ja kotipaikka
        print(f"{self._nimi}, {self._kotipaikka}")
        # tulostetaan jasenet
        print(f"Jäsenet:")
        for jasen in self._jasenet:
            print(jasen) 

if __name__ == "__main__":
    supermiekkonen = SuperSankari("Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()