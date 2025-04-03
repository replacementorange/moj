# TEE RATKAISUSI TÄHÄN:
class Havaintoasema():
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__havaintoja = 0
        self.__viimeisin_havainto = ""


    def __str__(self):
        return f"{self.__nimi}, {self.__havaintoja} havaintoa"

    def lisaa_havainto(self, havainto: str):
        self.__viimeisin_havainto = havainto
        self.__havaintoja += 1

    def viimeisin_havainto(self):
        return self.__viimeisin_havainto

    def havaintojen_maara(self):
        return self.__havaintoja

if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)