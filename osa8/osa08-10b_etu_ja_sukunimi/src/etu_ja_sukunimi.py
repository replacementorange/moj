# Tee ratkaisusi tähän:

# Voit olettaa metodeissa,
# että konstruktroissa annetussa nimessä on 
# etu- ja sukunimi välilyönnillä erotettuna eikä muita nimiä.
# split()

class Henkilo():
    # Konstruktori
    def __init__(self, nimi: str):
        self.nimi = nimi
    
    # Palauttaa etunimen
    def anna_etunimi(self):
        kokonimi = self.nimi.split()
        #print (kokonimi)
        return kokonimi[0]
    
    # Palauttaa sukunimen
    def anna_sukunimi(self):
        kokonimi = self.nimi.split()
        return kokonimi[1]

if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi()) 