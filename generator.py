import random

p = input("Podaj p:")
n = input("Podaj n:")

with open("dane.txt", "w") as f:
    f.write(str(p) + "\n")
    f.write(str(n) + "\n")
    for x in range(int(n)):
        f.write(str(random.randint(int(p),int(n))) + "\n")