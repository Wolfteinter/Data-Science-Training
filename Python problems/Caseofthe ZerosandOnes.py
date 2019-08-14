def function(n):
    n = list(n)
    bandera = True
    bandera2 = True
    while(True):
        for i in range(len(n) - 2):
            if(n[i] == '1' and n[i+1] == '0'):
                n.pop(i)
                n.pop(i+1)
                bandera2 = True
            elif(n[i] == '0' and n[i+1] == '1'):
                n.pop(i)
                n.pop(i+1)
                bandera2 = True
            else:
                bandera2 = False
        if(bandera2):
            break;
    print(len(n))
if __name__ == '__main__':
    n = int(input().strip())
    a = str(input().strip())
    print(a)
    function(a)
