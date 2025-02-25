# 행렬덧셈
N,M = map(int,input().split())
A =[]
for _ in range(N):
    A.append(list(map(int,input().split())))
B = []
for _ in range(N):
    B.append(list(map(int,input().split())))
for i in range(N):
    new = []
    for j in range(M):
        new.append(A[i][j]+B[i][j])
    print(*new)

# 최댓값
A = []
value = 0
row, col =0,0
for _ in range(9):
     A.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if A[i][j] > value:
            value = A[i][j]
            row , col = i , j
print(value)
print(row+1, col+1)

# 세로읽기
A=[]
B=[]
for _ in range(5):
    A.append(input().strip())
for i in range(max(map(len,A))):
    for j in range(5):
        if i < len(A[j]):
            B.append(A[j][i])
print("".join(B))


#1 색종이
T = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(T):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1
print(sum(sum(k) for k in paper))


