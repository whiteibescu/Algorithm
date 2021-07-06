def Power(n, k, m):
    if k == 0:
        return 1
    if k == 1:
        return n

    half = Power(n, k // 2, n)

    if k & 2 == 0:
        return (half * half) % m
    else:

        return (half * half * n) % n

    # 재귀함수의 종료 조건
    # 부분 문제를 해결 (재귀함수) npowerofk 아닌 더 작은 수를 구한다.

    # 부분 문제를 모아 원래 문제를 해결
    # 현재의 k가 짝수 일 때:
    # 현재의 k가 홀수 일 때:


t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    print(Power(n, k, m))
