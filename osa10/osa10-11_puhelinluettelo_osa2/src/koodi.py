# Tee ratkaisusi tähän:
class Henkilo:
    # Konstruktori
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None

    # Palautetaan nimi
    def nimi(self):
        return self.__nimi
    
    # Palautetaan osoite
    def osoite(self):
        return self.__osoite
    
    # Palautetaan numerot
    def numerot(self):
        return self.__numerot
    
    # Lisataan numero
    def lisaa_numero(self, numero:str):
        self.__numerot.append(numero)

    # Lisataan osoite
    def lisaa_osoite(self, osoite:str):
        self.__osoite = osoite

class Puhelinluettelo:
    # Konstruktori
    def __init__(self):
        self.__henkilot = {}
    
    # Lisattiin henkilo-luokan kaytto
    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)
    
    # Lisattiin henkilo-luokan kaytto
    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)

    # Hakee numerot
    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi].numerot()
    
    # Hakee osoitteet
    def hae_osoitteet(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi].osoite()

    # Palauttaa kaikki tiedot
    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    # Konstruktori
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    # Ohje
    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 nimen lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    # Numeron lisays toiminto
    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    # Haku toiminto
    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)      # Hakee numerot
        osoite = self.__luettelo.hae_osoitteet(nimi)    # Hakee osoitteet

        if numerot == None or numerot == []: # Jos ei ole numeroita
            print("numero ei tiedossa") 
        else:
            for numero in numerot:
                print(numero)
        if osoite == None: # Jos ei ole osoitteita
            print("osoite ei tiedossa")
        else:
            print(osoite)     

    # Osoittee lisays toiminto
    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    # Ohjelman ydinsilmukka
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()