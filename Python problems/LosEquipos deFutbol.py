from math import factorial
def main(n):
    if(n < 4):
        print(0)
        print(0)
    else:
        pos = factorial(n)/factorial(n - 4)
        print(pos)
        if(pos >= 2000):
            print(1)
        else:
            print(0)
if __name__ == '__main__':
    n = int(raw_input())
    main(n - 1)
