from random import randint

nazwaPliku = str(input('Nazwa: '))

p = input('\nPodaj p: ')
n = input('Podaj n: ')

zakresDol = int(input('\nZakres od: '))
zakresGora = int(input('Zakres do: '))

liczby = [str(randint(zakresDol, zakresGora)) for _ in range(int(n))]

with open("dane.txt", "w") as f:
    f.write(str(p) + "\n")
    f.write(str(n) + "\n")
    f.write("\n".join(liczby))