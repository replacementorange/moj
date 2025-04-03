# TEE RATKAISUSI TÄHÄN:
class Aanite():
    def __init__(self, pituus: int):
        if pituus < 0:
            raise ValueError
        else:
            self.__pituus = pituus

    # Havainnointimetodi
    @property
    def pituus(self):
        return self.__pituus

    # Asetusmetodi
    @pituus.setter
    def pituus(self, pituus):
        if pituus < 0:
            raise ValueError
        else:
            self.__pituus = pituus

if __name__ == "__main__":
    the_wall = Aanite(43)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)