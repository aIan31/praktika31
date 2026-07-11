import sys
from itertools import combinations
d = list(map(int, sys.stdin.buffer.read().split()))
if not d:
    exit()
n, k = d[0], d[1]
a = d[2:]
mx = 0
for c in combinations(a, k):
    x = 0
    for v in c:
        x ^= v
    if x > mx:
        mx = x
print(mx)