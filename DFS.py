t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u,v = map(int,input().split())
        List[u].append(v)
        List[v].append(u)

    for i in range(N):
        List[i].sort(reverse=True)

    Check = [False]*N
    Stack = [0]
    while Stack:
        v = Stack.pop()
        if Check[v] == True:
            continue

        Check[v] = True
        print(v, end=" ")
        for i in List[v]:
            if Check[i] == False:
                Stack.append(i)
    print("")