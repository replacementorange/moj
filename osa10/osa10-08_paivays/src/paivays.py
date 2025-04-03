# TEE RATKAISUSI TÄHÄN:
class Paivays():
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.__paiva = paiva
        self.__kuukausi = kuukausi
        self.__vuosi = vuosi

    # Palauttaa paivamaaran
    def __str__(self):
        return(f"{self.__paiva}.{self.__kuukausi}.{self.__vuosi}")

    # Vertailuoperaattorit < > == !=
    def __lt__(self, toinen: 'Paivays'):
        # verrataan paivat, kuukaudet ja vuodet keskenaan
        if self.__vuosi < toinen.__vuosi:
            return True
        elif self.__vuosi == toinen.__vuosi:
            if self.__kuukausi < toinen.__kuukausi:
                return True
            elif self.__kuukausi == toinen.__kuukausi:
                if self.__paiva < toinen.__paiva:
                    return True
        return False

    def __gt__(self, toinen: 'Paivays'):
        # Kaytetaan lt ja eq hyodyksi
        if self.__lt__(toinen) == False and self.__eq__(toinen) == False:
            return True
        return False

    def __eq__(self, toinen: 'Paivays'):
        # Katsotaan, etta paiva, kuukausi ja vuosi ovat yhtasuuria
        if self.__paiva == toinen.__paiva and \
            self.__kuukausi == toinen.__kuukausi and \
                self.__vuosi == toinen.__vuosi:
                return True
        return False

    def __ne__(self, toinen: 'Paivays'):
        # Kaytetaan hyvaksi ==
        if self.__eq__(toinen) == False:
            return True
        return False

    # Huomaa, että koska oletamme jokaisessa kuukaudessa olevan 30 päivää,
    # tässä tehtävässä vuosien päivien lukumäärä on 12*30 eli 360.
    # Tehdaan paivamuunnin
    def __paivamuunnin(self):
        return ((self.__vuosi - 1) * 12 * 30) + ((self.__kuukausi - 1) * 30) + self.__paiva # 360

    # Lisay
    # Muutetaan paiviksi ja lisataan
    def __add__(self, lisattavia_paivia: int):
        paivat = self.__paivamuunnin()
        paivat += lisattavia_paivia

        vuosi = (paivat // 360) + 1
        kuukausi = ((paivat // 30) % 12) + 1
        paiva = paivat % 30
        return Paivays(paiva, kuukausi, vuosi)

    # Vahennys
    # Muutetaan paiviksi ja vahennetaan
    def __sub__(self, toinen: 'Paivays'):
        paivia = self.__paivamuunnin()
        toinen_paivia = toinen.__paivamuunnin()
        return abs(paivia - toinen_paivia)


if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)