# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    # lasketaan henkiloiden summa
    h1 = (henkilo1["tulos1"] + henkilo1["tulos2"] + henkilo1["tulos3"]) / 3
    h2 = (henkilo2["tulos1"] + henkilo2["tulos2"] + henkilo2["tulos3"]) / 3
    h3 = (henkilo3["tulos1"] + henkilo3["tulos2"] + henkilo3["tulos3"]) / 3

    # Etsitaan pienin ka ja palautetaan se
    if h1 < h2 and h1 < h3:
        return henkilo1
    if h2 < h1 and h2 < h3:
        return henkilo2
    if h3 < h2 and h3 < h1:
        return henkilo3

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))