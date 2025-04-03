# https://docs.python.org/3/library/math.html
from math import sqrt

# TEE RATKAISUSI TÄHÄN:
def neliojuuret(luvut: list):
    return [sqrt(luku) for luku in luvut]

if __name__ == "__main__":
    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:
        print(rivi)