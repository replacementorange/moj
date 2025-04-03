# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur" # Lisataan :02d
    
    # Muutetaan rahat muotoon ee.sntsnt
    def __raha(self):
        return self.__eurot + (self.__sentit / 100)

    def __eq__(self, toinen: 'Raha'):
        return self.__raha() == toinen.__raha()

    def __lt__(self, toinen):
        return self.__raha() < toinen.__raha()

    def __gt__(self, toinen):
        return self.__raha() > toinen.__raha()

    def __ne__(self, toinen):
        return self.__raha() != toinen.__raha()

    # Lisaa
    def __add__(self, toinen):
        # Lasketeaan eurot
        eurot_yhteensa = self.__eurot + toinen.__eurot
        # Lasketeaan sentit
        sentit_yhteensa = self.__sentit + toinen.__sentit

        # Senttien pyoristykset
        if sentit_yhteensa >= 100:
            eurot_yhteensa += 1
        sentit_yhteensa = sentit_yhteensa % 100
        raha_olio = Raha(eurot_yhteensa, sentit_yhteensa)
        return raha_olio

    # Vahenna
    def __sub__(self, toinen):
        # Virhetarkistus
        if (self.__raha() < toinen.__raha()):
            raise ValueError("negatiivinen tulos ei sallittu")
        
        eurot_yhteensa = self.__eurot - toinen.__eurot
        
        # Senttien riittävyys
        if self.__sentit >= toinen.__sentit:
            sentit_yhteensa = self.__sentit - toinen.__sentit
        else:
            eurot_yhteensa -= 1
            sentit_yhteensa = self.__sentit + (100 - toinen.__sentit)

        raha_olio = Raha(eurot_yhteensa, sentit_yhteensa)
        return raha_olio

if __name__ == "__main__":
    e1 = Raha(4, 5)
    print(e1)
    e1.eurot = 1000
    print(e1)