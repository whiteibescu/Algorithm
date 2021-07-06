t = int(input())
for _ in range(t):
    n = int(input())
    queue = []  #매 테스트 케이스마드 빈 큐로 초기화
    head = 0    #큐의 가장 왼쪽 인덱스
    tail = 0    #큐의 가장 오른쪽 인덱스 + 1
    for i in range(n):
        qry = int(input())
        if qry == -1:
            print(queue[head])  #pop 후 출력
            head += 1   #왼쪽 인덱스 업데이트
        else:
            queue.append(qry)   #push
            tail += 1   #오른쪽 인덱스 업데이트