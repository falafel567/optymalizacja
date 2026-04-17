import random
import math
import copy

def wczytaj():
    try:
        with open("cmax/INSTANCES/NU_1_0050_25_8.txt", "r") as file:
            p = int(file.readline())
            n = int(file.readline())
            tablica = list(map(int, file.readline().split()))
            # for _ in range(n):
            #     liczba = int(file.readline())
            #     tablica.append(liczba)
            return p, tablica
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku test.txt")
        return 2, [10, 20, 30, 40, 50]


def zachlanny(p, tablica):
    t_koniec = [0] * p
    for gene in tablica:
        idx_min = t_koniec.index(min(t_koniec))
        t_koniec[idx_min] += gene
    return max(t_koniec)


if __name__ == '__main__':
    p, tablica = wczytaj()
    n = len(tablica)
    wynik = zachlanny(p, tablica)
    print("--- KONIEC ---")
    print(tablica)
    print(f"Najlepszy znaleziony czas: {wynik}")