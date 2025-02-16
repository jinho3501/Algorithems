N = int(input())
A = list(map(int,input().split()))
repairA = sorted(A)
P = [0] * N
used = [False] * N

for i in range(N):
    for j in range(N):
        if A[i] == repairA[j] and not used[j]:
            P[i] = j
            used[j] = True
            break
print(*P)

# A = list(map(int, input().split()))  # 원본 배열 A 입력받기
#
# sorted_A = sorted(A)  # A를 정렬하여 새로운 배열 생성
#
# # 각 값이 정렬된 배열에서 몇 번째 인덱스인지 찾기
# index_map = {value: idx for idx, value in enumerate(sorted_A)}
#
# # A의 원소를 차례대로 index_map에서 찾아서 P 배열 생성
# P = [index_map[value] for value in A]
#
# print(*P)  # 결과 출력