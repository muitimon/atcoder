N=int(input())
#xList=[]
oshita=0
longSet=set()
for i in range(N):
    now=input()
    for j in range(len(now)):
        if now[j]=='x':
            oshita=oshita+1
            longSet.discard(j)
        elif now[j]=='o':
            before=len(longSet)
            longSet.add(j)
            if before!=len(longSet):
                oshita=oshita+1
        else:
            longSet.discard(j)
print(oshita)

