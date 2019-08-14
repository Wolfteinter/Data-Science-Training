def main(x):
    val_max = 0
    val_min = 101
    pos_max = 0
    pos_min = 0
    for i in range(len(x)):
        if(x[i] < val_min):
            val_min = x[i]
            pos_min = i
        elif(x[i] == val_min):
            if(i > pos_min):
                pos_min = i
    pasos = 0
    while(pos_min != len(x)-1):
        x[pos_min],x[pos_min+1] = x[pos_min+1],x[pos_min]
        pos_min += 1
        pasos += 1

    for i in range(len(x)):
        if(x[i] > val_max):
            val_max = x[i]
            pos_max = i
        elif(x[i] == val_max):
            if(i < pos_max):
                pos_max = i

    while(pos_max != 0):
        x[pos_max],x[pos_max-1] = x[pos_max-1],x[pos_max]
        pos_max -= 1
        pasos += 1
    print(pasos)


if __name__ == '__main__':
    n = int(input())
    x = list(map(int,input().rstrip().split()))
    main(x)
