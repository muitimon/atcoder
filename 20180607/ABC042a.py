from collections import Counter
numlist=Counter(input().split())
if numlist.most_common()[0][0]=="5" and numlist.most_common()[0][1]==2:
    if numlist.most_common()[1][0]=="7" and numlist.most_common()[1][1]==1:
       print("YES")
else:
    print("NO")

