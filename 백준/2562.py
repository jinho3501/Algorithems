number =[]
for _ in range(9):
    n = int(input())
    number.append(n)
    asc_number = sorted(number,reverse = True)
    idx = number.index(asc_number[0])

print(f"{asc_number[0]}\n{idx+1}")

