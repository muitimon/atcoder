N=int(input())
flag=True
for i in range(2,int(N/2)+1):
    if N%i==0:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")
