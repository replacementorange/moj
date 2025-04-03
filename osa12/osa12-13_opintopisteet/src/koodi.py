from functools import reduce

# Huomaa, että Pythonin versiosta 3 alkaen funktio reduce pitää erikseen ottaa käyttöön moduulista functools

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Tee ratkaisusi tähän:
def kaikkien_opintopisteiden_summa(suorituskset: list):
    # lukujen_summa = reduce(lambda summa, alkio: summa + alkio, lista, 0)
    return reduce(lambda summa, alkio: summa + alkio.opintopisteet, suorituskset, 0)

def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    # laskee vain niiden suorituksien op:t joiden arvosana > 0
    # suoritusten opintopisteet (summa) --> suodatetaan ne jotka arvosana > 0
    return reduce(lambda summa, suoritus: summa + suoritus.opintopisteet, filter(lambda suoritus: suoritus.arvosana > 0, suoritukset), 0)

def keskiarvo(suoritukset: list):
    # alusta summa lambda lauseke --> summa + op, tarkista, etta arvosana on > 0 ja summa on aluksi 0
    # katso suoritettu = suorituset joiden arvosana > 0 list, filter
    # palauta niiden keskiarvo = reduce: lambda summa, jaettuna maaralla
    suoritettu = list(filter(lambda suoritus: suoritus.arvosana > 0, suoritukset)) # saadaan suoritukset jotka ovat lapi (arvosana > 0)
    return reduce(lambda summa, suoritus: summa + suoritus.arvosana, suoritettu, 0) / len(suoritettu) # lasketaan keskiarvo lapi menevilla

if __name__ == "__main__":
    #suoritus = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    #print(suoritus)
    #print(suoritus.kurssi)
    #print(suoritus.opintopisteet)
    #print(suoritus.arvosana)

    #s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    #s2 = Suoritus("Ohjelmoinnin jatkokutssi", 4, 5)
    #s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    #summa = kaikkien_opintopisteiden_summa([s1, s2, s3])
    #print(summa)

    #s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    #s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    #s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    #summa = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
    #print(summa)

    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)