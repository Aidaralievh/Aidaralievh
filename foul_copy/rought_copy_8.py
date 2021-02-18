
inputt = open('input.txt')
output = open('output.txt', 'w')
read = inputt.read().split()
a = [int(h) for h in read]
del a [0]



l = [0 for x in range(read)]
for i in range(len(a)):
    num = a[i]
    l[num] += 1


# hours = None
#
# for h in l:
#     for o in h:
#         hours = h[0] * 3600 + h[1]
#     g.append(hours)
#
#
# for f in range(0, len(g) - 1):
#     for j in range(0, len(g) - f - 1):
#         if g[j] > g[j + 1]:
#             g[j], g[j + 1] = g[j + 1], g[j]
#
# print(g)

