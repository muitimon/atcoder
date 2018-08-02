from collections import deque
N,K=map(int,input().split())
upDownList=deque([])
before=int(input())
count=0
#tobasu=K
for i in range(N-1):
    now=int(input())
#    if tobasu!=K:
#        print(i,before,now)
#        before=now
#        tobasu=tobasu+1
#        continue
    if before<now:
        upDownList.append(1)
#        print(i,before,now,"up")
    else:
 #       tobasu=1
        upDownList.clear()
#        print(i,before,now,"down")
#    print("len",len(upDownList))
    if len(upDownList)==K-1:
        count=count+1
        upDownList.popleft()
    before=now
print(count)
