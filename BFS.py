from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        List[u].append(v)
    for i in range(N):
        List[i].sort()

    Check = [False]*N # 방문했는지 안 했는지 확인
    Queue = deque([0]) # 큐
    while Queue:
        v = Queue.popleft() # 큐에서 나오는 v
        if Check[v] == True: # v가 이 시점에서 방문했다면
            continue
        Check[v] = True
        print(v, end=" ")
        for i in List[v]:   # v와 연결된 모든 장점 중
            if Check[i] == False: #아직 가지 않은 i가 있다면
                Queue.append(i)# 큐에 push
    print("")