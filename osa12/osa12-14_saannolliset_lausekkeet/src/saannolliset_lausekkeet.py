# TEE RATKAISUSI TÄHÄN:
import re

def on_viikonpaiva(merkkijono: str):
    # re.search ja | -->(Pystyviivalla voidaan erottaa vaihtoehtoisia osajonoja.)
    # Palautetaan True jos loytyy: "ma|ti|ke|to|pe|la|su", muuten False
    return re.search("ma|ti|ke|to|pe|la|su", merkkijono) is not None

def kaikki_vokaaleja(merkkijono: str):
    # Hakasulkeiden väliin voidaan merkitä joukko hyväksyttyjä merkkejä.
    # re.search + [] + vokaalit ja ei none
    # Merkillä ^ voidaan määritellä, että osuman pitää löytyä merkkijonon alusta, ja vastaavasti merkillä $, että sen on oltava lopussa.
    # * toistaa osaa minkä tahansa määrän kertoja (myös nolla)
    # alku, loppu, toista --> merkkijono
    return re.search("^[aeiouyöäå]*$", merkkijono) is not None

def kellonaika(merkkijono: str):
    # Merkintä [1-3][0-9] hyväksyy kaksinumeroiset luvut väliltä 10...39.
    # tt:mm:ss --> ([][]|[]) (h) : [][] (m) : [][] (s)
    # h <= 24, m <= 59, s <= 59 --> kirjaimet ei kay
    return re.search('([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', merkkijono) is not None

if __name__ == "__main__":
    #print(on_viikonpaiva("ma"))
    #print(on_viikonpaiva("pe"))
    #print(on_viikonpaiva("tu"))

    #print(kaikki_vokaaleja("eioueioieoieouyyyy"))
    #print(kaikki_vokaaleja("autoooo"))

    print(kellonaika("12:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))
