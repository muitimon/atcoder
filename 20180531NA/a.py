y = int(input())
m = int(input())
d = int(input())
if m==1:
    y=y-1
    m=13
elif m==2:
    y=y-1
    m=14
ans = 365*y + int(y/4) - int(y/100) + int(y/400) + int(306*(m+1)/10) + d - 429
print(735369-int(ans))
