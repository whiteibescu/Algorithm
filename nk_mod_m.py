t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    print(pow(n, k, m))
