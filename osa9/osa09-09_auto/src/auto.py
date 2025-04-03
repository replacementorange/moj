# TEE RATKAISUSI TÄHÄN:
class Auto():
    def __init__(self):
        self.__bensatankin_sisalto = 0
        self.__ajetut_km = 0

    def tankkaa(self):
        self.__bensatankin_sisalto = 60

    def aja(self, km: int):
        if km > self.__bensatankin_sisalto:
            km = self.__bensatankin_sisalto
        self.__ajetut_km += km
        self.__bensatankin_sisalto -= km

    def __str__(self):
        return f"Auto: ajettu {self.__ajetut_km} km, bensaa {self.__bensatankin_sisalto} litraa"

if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)