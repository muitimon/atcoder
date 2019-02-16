a,b=map(int,input().split())
tower=0
for i in range(1,b-a):
    tower=i+tower
print(tower-a)
