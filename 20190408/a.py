import collections
l = list()
while True:
    tmp = input()
    l.append(tmp)
    print(tmp)
    if tmp == "\n":
        break
c = collections.Counter(l)
max = c.most_common()[0][1]
i = 0
while max==c.most_common[i+1][1]:
    print(c.most_common[i][0])
    i = i + 1
