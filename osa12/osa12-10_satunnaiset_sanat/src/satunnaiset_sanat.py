# TEE RATKAISUSI TÄHÄN:
from random import choice

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return ("".join([choice(kirjaimet) for i in range(pituus)]) for j in range(maara))

if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)