import sys
s = sys.stdin.buffer.read().strip()
n = len(s)
pi = [0]*n
for i in range(1, n):
    j = pi[i-1]
    while j and s[i] != s[j]:
        j = pi[j-1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j
p = n-pi[-1]
if n % p:
    p = n
print(p)