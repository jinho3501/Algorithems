import math

def bridge(n,m):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
T = int(input())
for _ in range(T) :
    n, m = map(int,input().split())
    print(bridge(n,m))
 

    # math.comb를 사용하여 조합 사용
    # print(math.comb(m,n))
