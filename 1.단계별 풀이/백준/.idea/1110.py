num = int(input(""))
count = 0
result = num
while True:
    a = result // 10
    b = result % 10
    result = b * 10 + (a + b) % 10
    count += 1
    if result == num:
        break

print(count)
#====GPT 풀이========
# num = int(input())  # 입력받은 숫자 num
# result = num  # result는 처음에 num으로 설정
# count = 0
#
# while True:
#     result = (result % 10) * 10 + ((result // 10 + result % 10) % 10)
#     count += 1
#     if result == num:  # result가 다시 num과 같아지면 종료
#         break
#
# print(count)