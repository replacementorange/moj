# Tee ratkaisusi tähän:
class Tehtava():
    # Sailotaan tehtava ID
    tehtavia = 0

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.__valmis = False

        # Kasvatetaan tehtavan ID
        Tehtava.tehtavia += 1
        self.id = Tehtava.tehtavia
    
    # Palautetaan valmiustila
    def on_valmis(self):
        return self.__valmis

    # Asetetaan valmiusteksti
    def aseta_valmius(self):
        status = "EI VALMIS"
        if self.__valmis:
            status = "VALMIS"
        return status

    # Muutetaan valmiustilaa
    def merkkaa_valmiiksi(self):
        self.__valmis = True

    # Palautetaan tulostus
    def __str__(self):
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.aseta_valmius()}"

class Tilauskirja():
    def __init__(self):
        # Sailotaan tehtavat
        self.__tehtavat = []

    # Lisaa tilauksen, hyodyntaa Tehtava-luokkaa
    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        # tehtava
        tehtava = Tehtava(kuvaus, koodari, tyomaara)
        # Lisataan tehtava tehtaviin
        self.__tehtavat.append(tehtava)

    # Palauttaa kaikki tehtavat
    def kaikki_tilaukset(self):
        return self.__tehtavat
    
    # Palauttaa koodarit
    def koodarit(self):
        # https://ohjelmointi-24.mooc.fi/osa-11/2-lisaa-koosteesta
        return list(set([tehtava.koodari for tehtava in self.__tehtavat]))
    
    def merkkaa_valmiiksi(self, id: int):
        for tehtava in self.__tehtavat:
            if tehtava.id == id:
                tehtava.merkkaa_valmiiksi()
                return
        raise ValueError(f'Tehtavaa numeroltaan {id} ei ole')
    
    def valmiit_tilaukset(self):
        # https://ohjelmointi-24.mooc.fi/osa-11/2-lisaa-koosteesta + tavallinen bool tarkistus
        return [tehtava for tehtava in self.__tehtavat if tehtava.on_valmis() == True]

    def ei_valmiit_tilaukset(self):
        # https://ohjelmointi-24.mooc.fi/osa-11/2-lisaa-koosteesta
        return [tehtava for tehtava in self.__tehtavat if tehtava.on_valmis() == False]
    
    # palauttaa tuplen, joka kertoo koodarin valmistuneiden 
    # ja vielä valmistumattomien töiden määrän sekä näihin kuluneiden työtuntien summan
    def koodarin_status(self, koodari: str):
        # Tarkistus onko koodaria olemassa
        if koodari not in self.koodarit():
            raise ValueError(f"Koodaria {koodari} ei ole olemassa")

        # Arvojen alustus
        valmis = 0
        kesken = 0
        valmis_tyotunnit = 0
        kesken_tyotunnit = 0
        # tehtavien alustus
        # https://ohjelmointi-24.mooc.fi/osa-11/2-lisaa-koosteesta
        tehtavat = [tehtava for tehtava in self.__tehtavat if tehtava.koodari == koodari]

        # lasketaan tehdyt ja keskeneraiset tehtavat ja niiden tyotunnit
        for tehtava in tehtavat:
            # jos tehtava on suoritettu
            # Lisataan suoritus ja siihen kulunut tyomaara
            if tehtava.on_valmis():
                valmis += 1
                valmis_tyotunnit += tehtava.tyomaara
            # jos tehtava ei valmis
            # Listaan keskeneraisiin ja lisataan tunnit
            else:
                kesken += 1
                kesken_tyotunnit += tehtava.tyomaara
        # Palautetaan laskut tuplena
        return (valmis, kesken, valmis_tyotunnit, kesken_tyotunnit)

if __name__ == "__main__":
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)