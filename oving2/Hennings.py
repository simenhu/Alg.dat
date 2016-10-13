from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    # SKRIV DIN KODE HER
    toppnode = Node()
    for tuple in ordliste:
        #Henter ut ordet og posisjonen til ordets slutt
        ord = tuple[0]
        pos = tuple[1]

        #Sjekker om den første bokstaven i ordet er underlagt toppnoden
        if ord[0] not in toppnode.barn.keys():
            parent = Node()
            toppnode.barn[ord[0]] = parent
        else:
            parent = toppnode.barn[ord[0]]
        #Sjekker alle de påfølgene bokstavene i ordet
        for i in range(1, len(ord)):
            if ord[i] not in parent.barn.keys():
                child = Node()
                parent.barn[ord[i]] = child
            else:
                child = parent.barn[ord[i]]
            #Legger til pos dersom vi har nådd slutten av ordet
            if i == (len(ord)-1):
                child.posi.append(pos)

            parent = child

    return toppnode


def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER

    if ord[indeks] == '?' :
        #Hent alle barn
        fusion = []
        for b in node.barn.values():
            if indeks != len(ord) - 1:
                fusion.extend(posisjoner(ord, indeks + 1, b))
            else:
                fusion.extend((b).posi)
        return fusion

    else:
        if indeks != len(ord)-1:
            if ord[indeks] not in node.barn.keys():
                return []
            return posisjoner(ord, indeks+1, node.barn.get(ord[indeks]))
        else:
            if ord[indeks] not in node.barn.keys():
                return []
            return node.barn.get(ord[indeks]).posi

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()