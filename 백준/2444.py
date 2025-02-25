n = int(input())  # 다이아몬드의 중심 높이

# 위쪽 삼각형 (가운데 줄 포함)
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 아래쪽 역삼각형
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))