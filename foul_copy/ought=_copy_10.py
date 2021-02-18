num = int(input())
l = []
for x in range(num):
    x = input().split()
    x = [int(i) for i in x]
    l.append(x)
g = []

hours = None

for i in l:
    for h in i:
        hours = i[0] * 3600 + i[1]
    g.append(hours)

for o in range(0, len(g) - 1):
    for j in range(0, len(g) - o - 1):
        if g[j] > g[j + 1]:
            g[j], g[j + 1] = g[j + 1], g[j]

print(g)