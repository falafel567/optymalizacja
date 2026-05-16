import random

p = 10
n = 1500
zakres_dol = 0
zakres_gora = 50

liczby = [str(random.randint(int(zakres_dol), int(zakres_gora))) for _ in range(int(n))]

with open("dane.txt", "w") as f:
    f.write(str(p) + "\n")
    f.write(str(n) + "\n")
    f.write("\n".join(liczby))