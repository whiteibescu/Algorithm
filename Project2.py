from collections import deque
t = int(input())

for _ in range(t):
    car = list(map(int, input().split()))
    q = deque([])

    for c in car:
        if q == 0 or deque[0] != c:
            q.append(c)
        else:
            q.pop(c)

    if q:
        print("YES")
    else:
        print("NO")