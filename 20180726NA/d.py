N=int(input())
a=set(map(int, input().split()))
ansset=set()
for i in a:
    while True:
        i,mod=divmod(i,2)
        if mod!=0:
            ansset.add(i)
            break
print(len(ansset))
