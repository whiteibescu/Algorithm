t = int(input())
for _ in range(t):
    n = int(input())
    stk = []        #매 테스트 케이스마다 빈 스택으로 스택 초기화
    for _ in range(n):
        qry = int(input())
        if qry == -1:
            print(stk.pop())    #pop 후 출력
        else:
            stk.append(qry)     #push