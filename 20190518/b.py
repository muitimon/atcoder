N=int(input())
V=[int(i) for i in input().split()]
C=[int(i) for i in input().split()]
profits = 0
for i in range(N):
  profit = V[i]-C[i]
  if profit > 0:
    profits = profits + profit
print(profits)
