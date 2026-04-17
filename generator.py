import random

p = input("Podaj p: ")
n = input("Podaj n: ")
zakres_dol = input("Podaj zakres od: ")
zakres_gora = input("Podaj zakres do: ")

liczby = [str(random.randint(int(zakres_dol), int(zakres_gora))) for _ in range(int(n))]

with open("dane.txt", "w") as f:
    f.write(str(p) + "\n")
    f.write(str(n) + "\n")
    f.write(" ".join(liczby))