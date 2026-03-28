def wczytaj():
    p = int(input())
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    return p, arr

if __name__ == '__main__':
    p, arr = wczytaj()
    print(p)
    print(arr)

