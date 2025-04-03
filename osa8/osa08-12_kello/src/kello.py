# Tee ratkaisusi tähän:
class Kello:
    # Konstruktori
    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit

    
    # Muodostetaan merkkijono kuvaus
    # Lisatty tunnit
    # 00:00:00
    def __str__(self) -> str:
        return f"{self.tunnit:02}:{self.minuutit:02}:{self.sekunnit:02}"
    
    # Kellon tikittamisen logiikka
    def tick(self):
        self.sekunnit += 1
        # Jos 60s tulee tayteen, muutetaan se min
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1

        # Jos tulee 60min tayteen muutetaan se alkamaan alusta
        if self.minuutit == 60:
            self.minuutit = 0
            self.tunnit += 1
        # Jos tunneista tulee paiva tayteen asetetaan se alkamaan alusta
        if self.tunnit == 24:
            self.tunnit = 0

    # Asetetaan aika (sekunnit == 0)
    def aseta(self, tunnit: int, minuutit: int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0
    

if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)