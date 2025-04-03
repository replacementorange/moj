
def sulut_tasapainossa(merkkijono: str):
    # Maaritellaan sulkeet
    sulkeet = "()[]{}"

    # Otetaan kaikki muu paitsi sulkeet pois
    for merkki in merkkijono:
        if merkki not in sulkeet:
            merkkijono = merkkijono.replace(merkki, "")

    # Pohja
    if len(merkkijono) == 0:
        return True
    # Lisattu tarkistus
    if not (merkkijono[0] == '(' and merkkijono[-1] == ')') and not (merkkijono[0] == '[' and merkkijono[-1] == ']'):
        return False

    # poistetaan ensimmäinen ja viimeinen merkki
    return sulut_tasapainossa(merkkijono[1:-1])

if __name__ == "__main__":
    ok = sulut_tasapainossa("([([])])")
    print(ok)

    ok = sulut_tasapainossa("(python versio [3.7]) käytä tätä!")
    print(ok)

    # ei kelpaa sillä virheellinen loppusulku
    ok = sulut_tasapainossa("(()]")
    print(ok)


    # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)