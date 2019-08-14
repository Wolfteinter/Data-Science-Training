def main():
    n = int(input())
    t_m = 0
    t_c = 0
    for i in range(n):
        m,c = list(map(int,input().rstrip().split()))
        if(m>c):
            t_m += 1
        elif(c>m):
            t_c += 1
    if(t_m > t_c):
        print("Mishka")
    elif(t_c > t_m):
        print("Chris")
    else:
        print("Friendship is magic!^^")
if __name__ == '__main__':
    main()
