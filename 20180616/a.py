A,B=map(int, input().split())
cake_list=[0 for i in range(17)]
for i in range(1,17):
    if cake_list[i-1]!=1 and cake_list[i]==0 and cake_list.count(1)<A:
        cake_list[i]=1
    if cake_list[i-1]!=-1 and cake_list[i]==0 and cake_list.count(-1)<B:
        cake_list[i]=-1
if cake_list.count(1)==A and cake_list.count(-1)==B:
    print("Yay!")
else:
    print(":(")
