N=int(input())
S=input()
for i in range(1,N):
    l1=list(set(S[0:i]))
    print(set(l1))
    l2=list(set(S[i:N]))
    print(set(l2))
    l1.extend(l2)
    print(collections.Counter(l1))
    print()
