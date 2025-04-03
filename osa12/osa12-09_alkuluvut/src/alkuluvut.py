# TEE RATKAISUSI TÄHÄN:

def alkuluvut():
    luku = 2
    while True:
        for numero in range(2, luku):
            if luku % numero == 0:
                break
        else:
            yield luku
        luku += 1


if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))