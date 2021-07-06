import bisect
def find(l, x):
    i = bisect.bisect_left(l, x)
    if i != len(l) and l[i] == x:
        return i
    return -1

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    answer = [find(data, x) for x in query]
    print(*ans)
