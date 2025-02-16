def min_exercise(N,m,M,T,R):
    current = m
    time = 0
    total_time = 0

    if m + T > M :
        return -1
    while time < N :
        if current + T <= M:
            current += T
            time += 1
        else :
            current = max(current - R, m)
        total_time += 1

    return total_time

N,m,M,T,R = map(int,input().split())
print(min_exercise(N, m, M, T, R))

