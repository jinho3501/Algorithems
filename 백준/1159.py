num = int(input())
words = [input().strip() for _ in range(num)]

first_count= {}

for word in words:
    first = word[0]
    first_count[first] = first_count.get(first,0) +1

result = sorted([char for char, count in first_count.items() if count >= 5])
if result :
    print("".join(result))
else:
    print("PREDAJA")

