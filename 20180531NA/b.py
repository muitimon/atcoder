N, A, B = map(int, input().split())
next = "Ant"
while N>0:
    if next=="Ant":
        N=N-A
        next="Bug"
    else:
        N=N-B
        next="Ant"
if next=="Ant":
    win="Bug"
else:
    win="Ant"
print(win)
