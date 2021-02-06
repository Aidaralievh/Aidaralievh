m = int(input())
n = [int(input()) for p in range(m)]
l = [0 for i in range(-100, 101)]
for x in range(len(n)):
    num = n[x]
    l[num] += 1
new = []
for m in range(-100, 101):
    if l[m]:
        for n_ in range(l[m]):
            new.append(m)
print(new)