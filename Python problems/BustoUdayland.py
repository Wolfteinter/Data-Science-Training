def main():
    n = int(input())
    asientos = []
    for i in range(n):
        a = str(input())
        asientos.append(a)
    for i in range(n):
        for j in range(len(asientos)-1):
            if(asientos[i][j] == 'O' and asientos[i][j+1] == 'O'):
                print("enre")
                asientos[i][j:j+1].replace("OO", "++")
                break
    print(asientos)

if __name__ == '__main__':
    main()
