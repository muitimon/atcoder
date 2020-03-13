N,M = map(int,input().split())
likes = [0]*M
for n in range(N):
    K = [int(i) for i in input().split()]
    A = K[1:]
    for a in A:
        likes[a-1]+=1
result=0
for like in likes:
    if like == N:
        result+=1
print(result)
