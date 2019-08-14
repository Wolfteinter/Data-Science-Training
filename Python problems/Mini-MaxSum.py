def function(lista):
    lista = sorted(lista)
    maxi = 0
    mini = 0
    for i in range(len(lista)):
        if(i!=0):
            maxi += lista[i]
        if(i!=len(lista)-1):
            mini += lista[i]
    print(mini,maxi)
if __name__ == '__main__':
    lista = list(map(int,input().rstrip().split()))
    function(lista)
