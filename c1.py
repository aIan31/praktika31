import sys
d = sys.stdin.buffer.read().split()
if not d:
    exit()
t = int(d[0])
o = []
p = 1
for _ in range(t):
    n = int(d[p])
    p += 1
    a = []
    for i in range(1, n+1):
        a.append(str(i))
        a.append(str(n+2*i-1))
        a.append(str(n+2*i))
    o.append(' '.join(a))
sys.stdout.write('\n'.join(o))