# TEE RATKAISUSI TÄHÄN:
class Lottorivi():
    # Konstruktori
    def __init__(self, kierros: int, pelattu_rivi: list):
        self.__kierros = kierros
        self.__pelattu_rivi = pelattu_rivi
    
    def osumien_maara(self, pelattu_rivi: list):
        return len([numero for numero in pelattu_rivi if numero in self.__pelattu_rivi])
    
    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [numero if numero in self.__pelattu_rivi else -1 for numero in pelattu_rivi]

if __name__ == "__main__":
    oikea = Lottorivi(5, [1,2,3,4,5,6,7])
    oma_rivi = [1,4,7,11,13,19,24]

    print(oikea.osumien_maara(oma_rivi))

    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]

    print(oikea.osumat_paikoillaan(oma_rivi))