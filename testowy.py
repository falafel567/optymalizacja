import random
import math
import copy

# --- PARAMETRY ---
liczba_pokolen = 5000
rozmiar_populacji = 30
szansa_mutacji = 0.05
elityzm = 1


def wczytaj():
    try:
        with open("dane.txt", "r") as file:
            p = int(file.readline())
            n = int(file.readline())
            tablica = [int(file.readline()) for _ in range(n)]
        return p, tablica
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku test.txt")
        return 2, [10, 20, 30, 40, 50]


def populacja_pierwsza(n):
    tab = list(range(n))
    return random.sample(tab, n)


def zachlanny(osobnik, p, tablica):
    t_koniec = [0] * p
    for gene in osobnik:
        idx_min = t_koniec.index(min(t_koniec))
        t_koniec[idx_min] += tablica[gene]
    return max(t_koniec)


def krzyzowanie(osobnik1, osobnik2):
    size = len(osobnik1)
    a, b = sorted(random.sample(range(size), 2))

    def fill_child(p1, p2):
        child = ['_'] * size
        child[a:b] = p1[a:b]
        wyjatki = set(child[a:b])

        p2_genes = [gene for gene in p2 if gene not in wyjatki]

        idx = 0
        for i in range(size):
            if child[i] == '_':
                child[i] = p2_genes[idx]
                idx += 1
        return child

    return fill_child(osobnik1, osobnik2)


def mutacja(osobnik):
    nowy = osobnik[:]
    idx1, idx2 = random.sample(range(len(nowy)), 2)
    nowy[idx1], nowy[idx2] = nowy[idx2], nowy[idx1]
    return nowy


def selekcja_turniejowa(populacja_oceniona, k=3):
    turniej = random.sample(populacja_oceniona, k)
    turniej.sort(key=lambda x: x[0])
    return copy.deepcopy(turniej[0][1])


if __name__ == '__main__':
    p, tablica = wczytaj()
    n = len(tablica)

    osobniki = [populacja_pierwsza(n) for _ in range(rozmiar_populacji)]

    for gen_idx in range(liczba_pokolen):
        oceniona_populacja = []
        for o in osobniki:
            oceniona_populacja.append((zachlanny(o, p, tablica), o))

        oceniona_populacja.sort(key=lambda x: x[0])

        nowa_populacja = []

        for i in range(elityzm):
            nowa_populacja.append(copy.deepcopy(oceniona_populacja[i][1]))

        while len(nowa_populacja) < rozmiar_populacji:
            rodzic1 = selekcja_turniejowa(oceniona_populacja)
            rodzic2 = selekcja_turniejowa(oceniona_populacja)

            dziecko = krzyzowanie(rodzic1, rodzic2)

            if random.random() < szansa_mutacji:
                dziecko1 = mutacja(dziecko)

            nowa_populacja.append(dziecko)

        osobniki = nowa_populacja

    finalna_ocena = sorted([(zachlanny(o, p, tablica), o) for o in osobniki])
    print("--- KONIEC ---")
    print(tablica)
    print(f"Najlepszy znaleziony czas: {finalna_ocena[0][0], finalna_ocena[0][1]}")