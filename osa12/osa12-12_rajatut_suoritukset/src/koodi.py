class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"


def hyvaksytyt(suoritukset: list):
    return filter(lambda a: a.arvosana >= 1, suoritukset)

def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return filter(lambda a: a.arvosana == arvosana, suoritukset)

def kurssin_suorittajat(suoritukset: list, kurssi: str):
    # Toteuta funktio käyttäen funktioita filter ja map.
    # lajittele opiskelijat, suodata arvosanat > 0 ja tarkista kurssi
     return sorted(list(map(lambda s: s.opiskelijan_nimi, filter(lambda s: s.arvosana > 0 and s.kurssi == kurssi, suoritukset))))

if __name__ == "__main__":
    #s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    #s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    #s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)

    #for suoritus in hyvaksytyt([s1, s2, s3]):
    #    print(suoritus)

    #s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    #s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    #s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 3)
    #s4 = Suoritus("Olivia Ohjelmoija", "Johdatus yliopistomatematiikkaan", 3)

    #for suoritus in suoritus_arvosanalla([s1, s2, s3, s4], 3):
    #    print(suoritus)

    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Tietoliikenteen perusteet", 5)
    s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
    s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)

    for suoritus in kurssin_suorittajat([s1, s2, s3, s4], "Tietoliikenteen perusteet"):
        print(suoritus)