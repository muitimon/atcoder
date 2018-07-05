while True:
    T,D,L = map(int,input().split())
    if T==0 and D ==0 and L == 0:
        break
    x = [int(input()) for i in range(T)]
    beforeflag=0
    flag=0
    total=0
    for i in range(T):
        if x[i]>=L:
            flag=1
            if beforeflag!=D+1 and beforeflag!=0:
                total+=1
        elif x[i]<L and flag>0 and flag<=D:
            flag+=1
            total+=1
        else:
            flag=0
        beforeflag=flag
    print(total)
