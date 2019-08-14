from math import pow
def main(n,t):
    init = int(pow(10,n-1))
    last = int(pow(10,n))
    bandera = True
    for i in range(init,last):
        if i%t == 0:
            bandera = False
            print(i)
            break
    if(bandera):
        print("-1")
if __name__ == '__main__':
    n,t = list(map(int,input().rstrip().split()))
    main(n,t)
