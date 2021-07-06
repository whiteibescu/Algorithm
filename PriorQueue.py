import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    hq = []
    for _ in range(n):
        q = int(input())
        if q== -1:
            print(heapq.heappop(hq))
        else:
            heapq.heappush(hq,q)