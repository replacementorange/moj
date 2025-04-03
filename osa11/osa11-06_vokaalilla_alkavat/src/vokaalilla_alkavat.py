# TEE RATKAISUSI TÄHÄN:
# a, e, i, o, u, y, ä, ö --> aAeEiIoOuUyYäÄöÖåÅ
def vokaalilla_alkavat(sanat: list):
    return [sana for sana in sanat if sana[0] in 'aAeEiIoOuUyYäÄöÖåÅ']

if __name__ == "__main__":
    klista = ["auto","mopo","Etana","kissa","Koira","OMENA","appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)