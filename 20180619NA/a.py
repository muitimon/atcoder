R_0,W_0,C,R=map(int,input().split())
#x=(C*W_0-R_0)/R
for i in range(100):
    if C*W_0<=i*R:
        x=i
        break
print(x)

