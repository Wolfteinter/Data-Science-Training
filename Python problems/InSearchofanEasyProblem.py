def main(lista):
    bandera = False;
    for i in lista:
        if i == 1:
            bandera = True
            break
    if bandera:
        print("HARD")
    else:
        print("EASY")

if __name__ == '__main__':
    n = int(input())
    lista = list(map(int,input().rstrip().split()))
    main(lista)
