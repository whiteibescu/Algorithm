t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    print(max(l) - min(l))