N=int(input())
a_list=map(int, input().split())
divA=0
for a in a_list:
    while a%2==0:
        a=a/2
        divA+=1
print(divA)
