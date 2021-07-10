def cmp(x):
    return x[0]/x[1]
T = int(input())
for _ in range(T):
    N,C = map(int, input().split())
    liquidlist = []
    for i in range(N):
        liquidlist.append(tuple(map(int, input().split())))
        liquidlist.sort(key=cmp, reverse = True)
        maxg = 0
        for i in range(N):
            if:

            else:

            print(int(maxg))