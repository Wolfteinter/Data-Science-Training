def main(n):
    con = 0
    for i in range(n):
        a,b,c = list(map(int,input().strip().split()))
        if(a+b+c >= 2):
            con += 1
    print(con)
if __name__ == '__main__':
    n = int(input())
    main(n)
