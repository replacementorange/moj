# Tee ratkaisusi tähän:
class Maksukortti:

    # Konstruktori
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    # Palauttaa kortin saldon
    def __str__(self):
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"
    
    # Perusateria (2.60€)
    # Vahentaa saldolta perusaterian hinnan verran
    # jos saldoa riittaa
    def syo_edullisesti(self):
        if self.saldo >= 2.6:
            self.saldo -= 2.6

    # Kalliimpi ateria (4.60€)
    # Vahentaa saldolta kalliimman aterian
    # hinnan verran jos saldoa riittaa
    def syo_maukkaasti(self):
        if self.saldo >= 4.6:
            self.saldo -= 4.6

    # Lisaa kortille saldoa pyydetyn maaran
    def lataa_rahaa(self, maara):
        if maara < 0:
            raise ValueError("Kortille ei saa ladata negatiivista summaa")
        else:
            self.saldo += maara

# Osa 1
#kortti = Maksukortti(50)
#print(kortti)
#print("----------")

# Osa 2
#kortti = Maksukortti(50)
#print(kortti)

#kortti.syo_edullisesti()
#print(kortti)

#kortti.syo_maukkaasti()
#kortti.syo_edullisesti()
#print(kortti)
#print("----------")

# Osa 3
#kortti = Maksukortti(10)
#print(kortti)
#kortti.lataa_rahaa(15)
#print(kortti)
#kortti.lataa_rahaa(10)
#print(kortti)
#kortti.lataa_rahaa(200)
#print(kortti)
#kortti.lataa_rahaa(-1) # raise ValueError("Kortille ei saa ladata negatiivista summaa")
#print("----------")

# Osa 4
# Luo kortit
pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)

# P m, M e
pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()

# Tulosteet syomisen jalkeen
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)

# P lataa 20€
pekan_kortti.lataa_rahaa(20)

# M m
matin_kortti.syo_maukkaasti()

# Tulosteet toimintojen jalkeen
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)

# P e P e
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()

# M lataa 50€
matin_kortti.lataa_rahaa(50)

# Korttisaldot lopussa
print("Pekka:", pekan_kortti)
print("Matti:", matin_kortti)