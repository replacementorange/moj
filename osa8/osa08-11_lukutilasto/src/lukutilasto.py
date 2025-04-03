# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        # Vaihdettu listaan helpomman kayton takia
        self.lukulista = []

    # Lisaa luvun listaan
    def lisaa_luku(self, luku:int):
        self.lukulista.append(luku)

    # Palauttaa lukujen maaran
    def lukujen_maara(self):
        return len(self.lukulista)
    
    # Palauttaa lukujen summan
    def summa(self):
        summa = sum(self.lukulista)
        return summa
    
    # Palauttaa lukujen keskiarvon
    
    def keskiarvo(self):
        # Tarkistetaan, etta lukulista ei ole tyhja
        if len(self.lukulista) > 0:
            # Lasketaan keskiarvo summa / maara
            return float(sum(self.lukulista) / len(self.lukulista))

# -- PAAOHJELMA --
luvut = Lukutilasto()

# Maaritellaan parilliset ja parittomat
parilliset = Lukutilasto()
parittomat = Lukutilasto()

# Kysytaan kayttajalta lukuja
print("Anna lukuja:")
while True:
    luku = int(input())
    # jos syote -1 niin lopetetaan
    if luku == -1:
        break
    # Tarkistetaan onko luku jaollinen 2
    if luku % 2 == 0:
        # Lisataan parillisten joukkoon
        parilliset.lisaa_luku(luku)
    else:
        # Lisataan parittomien joukkoon
        parittomat.lisaa_luku(luku)
    # Ja lopuksi lisataan kaikki samaan summan ja ka avuksi
    luvut.lisaa_luku(luku)

# Tulosteaan summa, ka, parilliset ja parittomat
print(f"Summa: {luvut.summa()}")
print(f"Keskiarvo: {luvut.keskiarvo()}")
print(f"Parillisten summa: {parilliset.summa()}")
print(f"Parittomien summa: {parittomat.summa()}")