class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

# Jarjestetaan pituuden mukaan
def jarjesta_pituuden_mukaan(reitti: Kiipeilyreitti):
    return reitti.pituus

def pituuden_mukaan(reitit: list):
    return sorted(reitit, key=jarjesta_pituuden_mukaan, reverse=True)

# Vaikeuden mukaan
def jarjesta_vaikeuden_mukaan(reitti: Kiipeilyreitti):
    return [reitti.grade, reitti.pituus] #[reitti.pituus ,reitti.grade] -> [reitti.grade, reitti.pituus]

def vaikeuden_mukaan(reitit: list):
    return sorted(reitit, key=jarjesta_vaikeuden_mukaan, reverse=True)

# Tee ratkaisusi tähän:
if __name__ == '__main__':
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")

    reitit = [r1, r2, r3, r4]
    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)