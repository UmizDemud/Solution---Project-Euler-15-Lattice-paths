from math import factorial as fac

for i in range(int(input())):
    n, m = list(map(int, input().strip().split()))
    print(int(((fac(n+m)//fac(n))//(fac(m)))%((10**9) + 7)))
