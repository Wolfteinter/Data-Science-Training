def main(cad):
    if cad == "{}":
        print("0")
    else:
        lista = cad[1:len(cad)-1].split(",")
        for i in range(len(lista)):
            lista[i] = lista[i].replace(" ", "")
        print(len(set(lista)))
if __name__ == '__main__':
    cad = str(input())
    main(cad)
