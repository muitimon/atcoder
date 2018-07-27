NA,NB=map(int, input().split())
A=set(map(int, input().split()))
B=set(map(int, input().split()))
AandB=A&B
AorB=A|B
print(len(AandB)/len(AorB))
