N,M = map(int,input().split())
bucket = [0] * N
for a in range(N):
    bucket[a] = a+1
for b in range(M):
    i,j = map(int,input().split())
    while i < j:
        bucket[i-1],bucket[j-1]=bucket[j-1],bucket[i-1]
        i += 1
        j -= 1
print(*bucket)