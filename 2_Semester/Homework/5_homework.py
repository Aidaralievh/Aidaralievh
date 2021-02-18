inputt = open('input.txt')
output = open('output.txt', 'w')
read = inputt.read().split()
a = [int(h) for h in read]
del a[0]
print(a)

l = [0 for i in range(-100, 101)]
for x in range(len(a)):
    num = a[x]
    l[num] += 1
new = []
for m in range(-100, 101):
    if l[m]:
        for n_ in range(l[m]):
            new.append(m)
print(new)
