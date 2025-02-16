count = 0  # "F"의 개수를 셀 변수
for i in range(8):
    chess = input().strip()  # 각 행을 입력받음
    for j in range(8):
        # (i + j) % 2는 해당 위치가 짝수 칸 또는 홀수 칸을 나타냄
        if (i + j) % 2 == 0:  # 짝수 칸에서 F가 있어야함
            if chess[j] == "F":
                count += 1
print(count)
