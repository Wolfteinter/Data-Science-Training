def main(n):
    i = 1
    z = 2
    suma = 1
    l = 0
    while(True):
        if(suma <= n):
            i += z
            suma+=i
            z += 1
            l += 1
        else:
            break;
    print(l)
if __name__ == '__main__':
    n = int(input())
    main(n)
