# Tee ratkaisusi luokan Koesuoritus perään.
# ÄLÄ MUUTA LUOKKAA
class Koesuoritus:
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet

    def __str__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'

# TEE RATKAISUSI TÄHÄN:
def hyvaksytyt(suoritukset: list, pisteraja: int):
    hyvaksyttyjen_lista = []

    # Kaydaan lapi suoritukset for-silmukalla
    for suoritus in suoritukset:
        # Jos suorituksen pisteet ovat == tai >, tallennetaan listaan
        if suoritus.pisteet >= pisteraja:
            hyvaksyttyjen_lista.append(suoritus)
    # Palautetaan lista, jossa on hyvaksytyt suoritukset
    return hyvaksyttyjen_lista


if __name__ == "__main__":
    s1 = Koesuoritus("Pekka", 12)
    s2 = Koesuoritus("Pirjo", 19)
    s3 = Koesuoritus("Pauli", 15)
    s4 = Koesuoritus("Pirkko", 9)
    s5 = Koesuoritus("Petriina", 17)

    hyv = hyvaksytyt([s1, s2, s3, s4, s5], 15)
    for hyvaksytty in hyv:
        print(hyvaksytty)