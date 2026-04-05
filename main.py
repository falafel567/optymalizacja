import random
import math

def wczytaj():
    with open("test.txt", "r") as file:
        p = int(file.readline())
        n = int(file.readline())
        tablica = []
        for _ in range(n):
            liczba = int(file.readline())
            tablica.append(liczba)

    # print(f"p: {p}, n: {n}")
    # print(f"Tablica: {tablica}\n")
    return p, tablica

def populacja_pierwsza(n):
    tab = [x for x in range(0, n)]
    osobnik = random.sample(tab, n)
    return osobnik

def zachlanny(osobnik, p, tablica):
    t_koniec = [tablica[osobnik[i]] for i in range(p)]
    for zadanie in range(p, len(osobnik)):
        t_koniec[t_koniec.index(min(t_koniec))] += tablica[osobnik[zadanie]]
    return max(t_koniec)

def krzyzowanie(osobnik1, osobnik2):
    swap1 = random.randint(0, len(osobnik1) - 1)
    swap2 = random.randint(0, len(osobnik1) - 1)
    while swap1 == swap2:
        swap2 = random.randint(0, len(osobnik1) - 1)
    osobnik_new = osobnik1[min(swap1, swap2):max(swap1, swap2)]
    wyjatki = set()
    for x in range(min(swap1, swap2), max(swap1, swap2)):
        wyjatki.add(osobnik1[x])
    for x in range(0, len(osobnik2)):
        if osobnik2[x] not in wyjatki:
            osobnik_new.append(osobnik2[x])
    del wyjatki
    return osobnik_new

def mutacja(osobnik):
    swap1 = random.randint(0, len(osobnik) - 1)
    swap2 = random.randint(0, len(osobnik) - 1)
    while swap1 == swap2:
        swap2 = random.randint(0, len(osobnik) - 1)
    temp = osobnik[swap1]
    osobnik[swap1] = osobnik[swap2]
    osobnik[swap2] = temp
    return osobnik

if __name__ == '__main__':
    p, tablica = wczytaj()
    #tablica czasow
    t_max = []
    osobniki = []

    #tworzenie nowej populacji o rozmiarze p
    for i in range(p):
        osobniki.append(populacja_pierwsza(len(tablica)))

    # #algorytm zachlanny
    for key, osobnik in enumerate(osobniki):
        t_max.append((zachlanny(osobnik, p, tablica), key))
    t_max.sort(key=lambda x: x[0])
    do_usuniecia = []
    for x in range(math.ceil(len(t_max)/2), len(t_max)):
        do_usuniecia.append(t_max[x][1])
    do_usuniecia.sort(reverse=True)
    for usun in do_usuniecia:
        osobniki.pop(usun)

    #glowna petla programu
    while len(osobniki) > 1:
        do_roboty = len(osobniki)
        for _ in range(0, do_roboty, 2):
            osobniki.append(krzyzowanie(osobniki[0], osobniki[1]))
            osobniki.pop(0)
            osobniki.pop(0)
        for osobnik in osobniki:
            osobnik = mutacja(osobnik)
    print(f"T_max: {zachlanny(osobniki[0], p, tablica)}")