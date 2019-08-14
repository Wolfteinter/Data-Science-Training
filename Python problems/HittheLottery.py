def main(n):
    monedas = [1,5,10,20,100]
    em = 4
    c = 0
    while(n != 0):
        if(n >= monedas[em]):
            n -= monedas[em]
            c += 1
        else:
            em -= 1
    print(c)
if __name__ == '__main__':
    n = int(input())
    main(n)
