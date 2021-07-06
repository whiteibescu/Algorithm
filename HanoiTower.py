def Hanoi(n, start, mid, end):
    if n == 1:
        return
    Hanoi(n-1, start, end, mid)
    Hanoi(start, '->', end)
    Hanoi(n-1, mid, start, end)

T = int(input())
for _ in range(T):
    n = int(input())
    Hanoi(n, 'A', "B", "C")
