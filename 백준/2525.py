H,M = map(int,input().split())
need_time = int(input())
total = (H * 60) + M + need_time

H = (total // 60) % 24
M = total % 60
print(H,M)