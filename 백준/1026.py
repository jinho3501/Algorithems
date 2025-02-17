N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
rB = sorted(range(len(B)), key= lambda i:B[i])
P = [0] * N
for i in range(N):
    P[rB[i]]=A[i]
result = sum(P[i]*B[i] for i in range(N))
print(result)