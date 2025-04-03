# TEE RATKAISUSI TÄHÄN:
def suodata_kielletyt(merkkijono: str, kielletyt: str):
    suodatettu = [merkki for merkki in merkkijono if merkki not in kielletyt]
    return ''.join(suodatettu)

if __name__ == "__main__":
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)