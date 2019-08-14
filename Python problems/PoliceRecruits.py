def main(lista):
    force = 0
    mal = 0
    for i in lista:
        if i < 0:
            if force >= abs(i):
                force -= abs(i)
            else:
                mal += abs(i)
        elif i > 0:
            force += i
    print(mal)


if __name__ == '__main__':
    n = int(input())
    lista = list(map(int,input().rstrip().split()))
    main(lista)
