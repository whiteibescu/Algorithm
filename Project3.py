import bisect

def find(l, x):
    i = bisect.bisect(l, x)
    if i == 0:
        return l[0]
    elif i == len(l):
        return l[i - 1]
    else:
        sub1 = x - l[i - 1]
        sub2 = l[i] - x
        if sub1 <= sub2:
            return l[i - 1]
        elif sub1 > sub2:
            return l[i]

t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    q = list(map(int, input().split()))
    ans = [find(l,x) for x in q]
    print(*ans)
