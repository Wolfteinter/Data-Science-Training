def main(n,x):
    c = 0
    for i in range(1,n+1):
        if(x % i == 0):
            c += 1
    print(c)
if __name__ == '__main__':
    n,x = list(map(int,input().rstrip().split()))
    main(n,x)
