import random
import math
import copy

liczba_pokolen = 5000
rozmiar_populacji = 50
szansa_mutacji = 0.2

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
    swap1 = random.randint(0, len(osobnik1)-1)
    swap2 = random.randint(0, len(osobnik1)-1)
    while swap1 == swap2 or (swap1 == 0 and swap2 == len(osobnik1)-1) or (swap2 == 0 and swap1 == len(osobnik1)-1):
        swap2 = random.randint(0, len(osobnik1)-1)
    #print(swap1, swap2)
    osobnik1_new = ['_' for _ in range(len(osobnik1))]
    wyjatki = set()
    for x in range(min(swap1, swap2), max(swap1, swap2)):
        osobnik1_new[x] = osobnik1[x]
        wyjatki.add(osobnik1[x])
    #print(osobnik1_new)
    osobnik_copy = copy.deepcopy(osobnik2)
    #print(osobnik_copy)
    to_del = []
    for ind in range(len(osobnik1_new)):
        if osobnik_copy[ind] in wyjatki:
           to_del.append(ind)
    to_del.sort(reverse=True)
    for usun in to_del:
        osobnik_copy.pop(usun)
    for i in range(len(osobnik1_new)):
        if osobnik1_new[i] == '_':
            osobnik1_new[i] = osobnik_copy[0]
            osobnik_copy.pop(0)
    #print(osobnik1_new)
    del wyjatki

    osobnik2_new = ['_' for _ in range(len(osobnik1))]
    wyjatki = set()
    for x in range(min(swap1, swap2), max(swap1, swap2)):
        osobnik2_new[x] = osobnik2[x]
        wyjatki.add(osobnik2[x])
    #print(osobnik2_new)
    osobnik_copy = copy.deepcopy(osobnik1)
    #print(osobnik_copy)
    to_del = []
    for ind in range(len(osobnik2_new)):
        if osobnik_copy[ind] in wyjatki:
            to_del.append(ind)
    to_del.sort(reverse=True)
    for usun in to_del:
        osobnik_copy.pop(usun)
    for i in range(len(osobnik2_new)):
        if osobnik2_new[i] == '_':
            osobnik2_new[i] = osobnik_copy[0]
            osobnik_copy.pop(0)
    #print(osobnik2_new)
    del wyjatki
    return osobnik1_new, osobnik2_new

def mutacja(osobnik):
    swap1 = random.randint(0, len(osobnik)-1)
    swap2 = random.randint(0, len(osobnik)-1)
    while swap1 == swap2:
        swap2 = random.randint(0, len(osobnik)-1)
    osobnik[swap1], osobnik[swap2] = osobnik[swap2], osobnik[swap1]
    return osobnik

if __name__ == '__main__':
    p, tablica = wczytaj()
    #tablica czasow
    t_max = []
    osobniki = []

    #tworzenie nowej populacji o rozmiarze rozmiar_populacji
    for i in range(rozmiar_populacji):
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
    t_max.clear()
    do_usuniecia.clear()

    #glowna petla programu
    i = 0
    while i < liczba_pokolen:
        osobniki_nowe = [osobniki[0]]
        random.shuffle(osobniki)
        for x in range(0, len(osobniki) - 1, 2):
            o1, o2 = krzyzowanie(osobniki[x], osobniki[x + 1])
            osobniki_nowe.extend([o1, o2])
        if len(osobniki_nowe) != rozmiar_populacji:
            osobniki_nowe.append(mutacja(osobniki_nowe[0]))
        for key, osobnik in enumerate(osobniki_nowe):
            if random.random() < szansa_mutacji:
                osobniki_nowe[key] = mutacja(osobnik)
        osobniki = copy.deepcopy(osobniki_nowe)
        for key, osobnik in enumerate(osobniki):
            t_max.append((zachlanny(osobnik, p, tablica), key))
        t_max.sort(key=lambda x: x[0])
        do_usuniecia = []
        for x in range(math.ceil(len(t_max) / 2), len(t_max)):
            do_usuniecia.append(t_max[x][1])
        do_usuniecia.sort(reverse=True)
        for usun in do_usuniecia:
            osobniki.pop(usun)
        if i == liczba_pokolen-1:
            print(t_max[0][0])
        t_max.clear()
        do_usuniecia.clear()
        i+=1
