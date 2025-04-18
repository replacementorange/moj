# TEE RATKAISUSI TÄHÄN:
class Kauppalista:
    def __init__(self):
        self.tuotteet = []
    
    def __iter__(self):
        self.t = 0
        return self

    def __next__(self):
        if self.t < len(self.tuotteet):
            tuote = self.tuotteet[self.t]
            self.t += 1
            return tuote
        else:
            raise StopIteration

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    for tuote in lista:
        print(f"{tuote[0]}: {tuote[1]} kpl")