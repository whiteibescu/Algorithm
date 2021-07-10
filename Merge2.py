def merge(left, right):
    result = []
    while len(list1)>0 < list2[0]:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

        if (len(list1) > 0):
            return result + list1
        else:
            return result + list2

t = int(input())
for _ in range(t):
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    answer = merge(list1, list2)
    print(answer)