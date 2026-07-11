import sys
d = list(map(int, sys.stdin.buffer.read().split()))
if not d:
    exit()
t = d[0]
p = 1
o = []
for _ in range(t):
    n = d[p]
    k = d[p+1]
    p += 2
    mx = 0
    for i in range(k):
        x = d[p+i]
        if x > mx:
            mx = x
    p += k
    o.append(str(2*(n-mx)-(k-1)))
sys.stdout.write('\n'.join(o))