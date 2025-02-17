N,M = map(int,input().split())
min_P = float('inf')
min_S = float('inf')
for i in range(M):
    pack , single = map(int,input().split())
    min_P = min(min_P,pack)
    min_S = min(min_S,single)

total = (N//6)*min_P
if N % 6 != 0:
    total += min(min_P,(N%6)*min_S)
total = min(total,(N*min_S))
print(total)