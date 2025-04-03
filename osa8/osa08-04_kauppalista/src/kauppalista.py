# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kauppalista!
# Kirjoita ratkaisusi luokan alapuolelle!
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

# ----------------------
# Tee ratkaisusi tähän:
# ----------------------
def tuotteita_yhteensa(lista: Kauppalista):
    # Alustetaan tuotteiden maara
    tuote_maara = 0

    # For-silmukan avulla lisataan tuotteisiin tuotteita
    # indeksointi alkaa 1
    for tuote in range(1, lista.tuotteita() + 1):
        # Lisataan tuotteisiin tuote listan avulla
        tuote_maara = tuote_maara + lista.maara(tuote)
    # Palautetaan laskettu maara
    return tuote_maara


if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    print(tuotteita_yhteensa(lista))