# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

    # Tämä mahdollistaa kirjaolion järkevän tulostamisen print-funktiolla
    def __repr__(self):
        return f"{self.nimi} ({self.kirjoittaja}), {self.kirjoitusvuosi} - genre: {self.genre}"

# -----------------------------
# tee ratkaisu tänne
def genren_kirjat(kirjat: list, genre: str):
    # Uusi lista
    kirjat_genrettain = []

    # Kaydaan For-silmukalla lapi kaikki kirjat
    # ja kerataan vain vaadittu genge
    for kirja in kirjat:
        if kirja.genre == genre:
            kirjat_genrettain.append(kirja)
    # Palautetaan lista
    return kirjat_genrettain

if __name__ == "__main__":
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    kirjat = [python, everest, norma, Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)]

    print("rikoskirjoja ovat")
    for kirja in genren_kirjat(kirjat, "rikos"):
        print(f"{kirja.kirjoittaja}: {kirja.nimi}")