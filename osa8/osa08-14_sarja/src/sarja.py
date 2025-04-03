# Tee ratkaisusi tähän:
class Sarja():

    # Konstruktori
    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelu = []
    
    def __str__(self):
        genret = ", ".join(self.genret)
        if self.arvostelu:
            return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {genret} \narvosteluja {len(self.arvostelu)}, keskiarvo {sum(self.arvostelu)/len(self.arvostelu):.1f} pistettä"
        else:
            return f"{self.nimi} ({self.kaudet} esityskautta) \ngenret: {genret} \nei arvosteluja"

    def keskiarvo(self):
        return sum(self.arvostelu) / len(self.arvostelu)    
    
    def arvostele(self, arvosana: int):
        if arvosana >= 0:
            self.arvostelu.append(arvosana)

def arvosana_vahintaan(arvosana: float, sarjat: list):
    arvosana_lista = []
    for sarja in sarjat:
        if arvosana <= sarja.keskiarvo():
            arvosana_lista.append(sarja)
    return arvosana_lista

def sisaltaa_genren(genre: str, sarjat: list):
    genre_lista = []
    for sarja in sarjat:
        if genre in sarja.genret:
            genre_lista.append(sarja)
    return genre_lista


if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)