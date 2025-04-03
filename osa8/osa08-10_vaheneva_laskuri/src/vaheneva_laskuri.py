# Tee ratkaisusi tähän:
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.alkuarvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        # Tarkistetaan, etta arvo on suurempi kuin 0
        if self.arvo > 0:
            # Vahennetaan arvosta
            self.arvo = self.arvo - 1

    # ja tänne muut metodit
    def nollaa(self):
        # vahennetaan arvosta sen arvo
        self.arvo = self.arvo - self.arvo
    
    def palauta_alkuperainen_arvo(self):
        # Kaytetaan konstruktoriin lisattya alkuarvoa
        self.arvo = self.alkuarvo

if __name__ == "__main__":
    laskuri = VahenevaLaskuri(55)
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.tulosta_arvo()
    laskuri.palauta_alkuperainen_arvo()
    laskuri.tulosta_arvo()