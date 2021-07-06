def hanoi(N, start, mid, end):
    if N == 1:
        print(f"{start} -> {end}")
    else:
        hanoi(N-1, start, end, mid)
        hanoi(1, start, mid, end)
        hanoi(N-1, mid, start, end)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    hanoi(N, 'A', 'B', 'C')
