def dividing():
    a,b = map(int, input().rstrip().split())
    a = list(str(a))
    c = len(a) - 1
    while(b > 0):
        if(a[c] == 0):
            c -= 1
        else:
            a[c] = (int(a[c]) - 1)
        b -= 1
    print(str(a[0:c]))
if __name__ == "__main__":
    dividing()
