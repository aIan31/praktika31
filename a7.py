import sys
d = sys.stdin.buffer.read().split()
if not d:
    exit()
t = int(d[0])
p = 1
o = []
for _ in range(t):
    n = int(d[p])
    a = int(d[p+1])
    b = int(d[p+2])
    p += 3
    o.append(str(min(n*a, (n//2)*b+(n % 2)*a)))
sys.stdout.write('\n'.join(o))