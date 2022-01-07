s = set()
a = [3,6,6,7,8]
d = dict()
for i in range(len(a)):
    t = 0
    for j in range(i, len(a)):
        t += a[j]
        d[t] = d.get(t, 0) + 1
p = 0
for k, v in d.items():
    if v ==1:
        p += k
print(p)
