T = int(input())
for _ in range(T):
    N = int(input())
    #T[i]: i번째 돌다리에 도달하는 경우의 수
    T = [0] * (N + 1)
    for i in range(1, N+1):
        if i == 1:
            T[1] = 1
        elif i == 2:
            T[2] = 2
        elif i == 3:
            T[3] = 4
        else:
            T[i] = (T[i - 1] + T[i - 2] + T[i-3]) % 1904101441
    print(T[N])