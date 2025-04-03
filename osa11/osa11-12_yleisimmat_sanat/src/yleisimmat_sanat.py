# TEE RATKAISUSI TÄHÄN:
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    # Luetaan tekstitiedosto
    with open(tiedoston_nimi, "r") as tiedosto:
        teksti = tiedosto.read()

    # Erikoismerkit
    erikoismerkit = ",.-'"
    suodatettu_teksti = ""

    # Kaydaan lapi tekstin merkkijonot (suodatus)
    for merkkijono in teksti:
        # Jos ei ole merkkijono niin lisataan suodatettuun
        if merkkijono not in erikoismerkit:
            suodatettu_teksti = suodatettu_teksti + merkkijono

    # Poistetaan valit ja rivivaihdot
    suodatettu_teksti = suodatettu_teksti.replace("\n", " ")
    suodatettu_teksti = suodatettu_teksti.split(" ")

    # Muodostetaan sanakirja ja palautetaan se
    sanakirja = {sana: suodatettu_teksti.count(sana) for sana in suodatettu_teksti if suodatettu_teksti.count(sana) >= raja}
    return sanakirja

if __name__ == "__main__":
    yleisimmat_sanat("comprehensions.txt", 3) #{'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}