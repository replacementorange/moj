# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    # Maaritetaan summa muokkamaan saatua matriisia
    summa = matriisi

    # Kaydaan kaikki matriisin rivit lapi ja lasketaan ne yhteen
    i = 0
    for rivi in matriisi:
        rivi.append(sum(rivi)) # [a, b] --> [a, b, a+b]
        summa[i] = rivi
        i = i + 1

if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)