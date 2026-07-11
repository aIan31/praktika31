import sys


def f(n, m={1: 0}):
    if n in m:
        return m[n]
    b = n*(n+1)//2-1
    for d in (2, 3):
        r = n % d
        v = n-r
        if v >= d:
            c = r*(2*n-r+1)//2+v+f(v//d)
            if c < b:
                b = c
    m[n] = b
    return b


print(f(int(sys.stdin.readline())))