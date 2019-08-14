import math
def main(n):
    lista=['Sheldon','Leonard','Penny','Rajesh','Howard']
    i= 5;
    while n>=i:
        print(n,i)
        n-=i
        i*= 2
    print(n,i)
    print(lista[int(n/(i/5))])
if __name__ == '__main__':
    n = int(input()) - 1
    main(n)
