s = set()
a = [3,6,6,7,8]
p = 0
for i in range(len(a)):
    t = 0
    for j in range(i, len(a)):
        t += a[j]
        print(t, s)
        if t not in s:
            p += t
        s.add(t)

print(sum(s))
