# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0
    
    # Muodostetaan merkkijono kuvaus
    def __str__(self) -> str:
        return f"{self.minuutit:02}:{self.sekunnit:02}"
    
    def tick(self):
        self.sekunnit += 1
        # Jos 60s tulee tayteen, muutetaan se min
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
        # Jos tulee 60min tayteen muutetaan se alkamaan alusta
        if self.minuutit == 60:
            self.minuutit = 0


if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()