
def main(n,k):
    if(n % 2 == 1):
        imp = ((n - 1)/2)+1
        par = imp - 1
    else:
        imp = n/2
        par = imp
    #No usar for
    imp = int(imp)
    par = int(par)
    if(k <= imp):
        print(2*(k) - 1)
    else:
        print(2*abs(k-imp))

if __name__ == '__main__':
    res = list(map(int, input().rstrip().split()))
    n,k = res[0],res[1]
    main(n,k)
