import random

def wczytaj():
    with open("dane.txt", "r") as file:
        p = int(file.readline())
        n = int(file.readline())
        tablica = []
        for _ in range(n):
            liczba = int(file.readline())
            tablica.append(liczba)

    print(f"p: {p}, n: {n}")
    print(f"Tablica: {tablica}\n")
    return p, tablica

def populacja_pierwsza(tablica):
    osobnik = random.sample(tablica, len(tablica))
    print(f"osobnik: {osobnik}")
    return osobnik

def zachlanny(osobnik, p):
    t_koniec = [osobnik[i] for i in range(p)]
    #print(f"t_koniec: {t_koniec}\n")
    for zadanie in range(p, len(osobnik)):
        t_koniec[t_koniec.index(min(t_koniec))] += osobnik[zadanie]
        #print(t_koniec)
    return max(t_koniec)


if __name__ == '__main__':
    p, tablica = wczytaj()
    osobniki = []
    for i in range(p):
        osobniki.append(populacja_pierwsza(tablica))
    print(f"osobniki: {osobniki}")
    t_max = []
    for osobnik in osobniki:
        t_max.append((zachlanny(osobnik, p), osobnik))
        print("\n")
    t_max.sort(key=lambda x: x[0])
    print(t_max)

