def main():
    t = int(input())
    for i in range(t):
        n,k = list(map(int,input().rstrip().split()))
        c = 0
        while(n != 0):
            if(n%k == 0):
                n /= k
            else:
                n -= 1
            c += 1
        print(c)
if __name__ == '__main__':
    main()
