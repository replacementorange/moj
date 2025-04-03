# tee ratkaisu tänne
# Muista import-lause:
# from datetime import date
from datetime import date

def vuodet_listaan(paivamaarat: list):
    # Alustetaan uusi lista
    vuodet = []

    # Kaydaan lapi paivamaarat for-silmukan avulla
    # Lisataan paivan vuosi vuosi-listaan
    for paiva in paivamaarat:
        vuodet.append(paiva.year)
        #print(vuodet)
    
    # Lajitellaan lista palauttamaan vuodet suuruusjarjestyksessa (pienemmasta suurimpaan)
    vuodet.sort()

    return vuodet

if __name__ == "__main__":
    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    print(vuodet) # [1993, 2006, 2019]