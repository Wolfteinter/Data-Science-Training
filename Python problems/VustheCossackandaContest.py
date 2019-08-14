def main(n,m,k):
    if(m>=n and k>=n):
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    n,m,k = list(map(int,input().strip().split()))
    main(n,m,k)
