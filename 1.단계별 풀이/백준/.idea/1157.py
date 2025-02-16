syn = input("").lower()
count = {}

for char in syn:
    count[char] = count.get(char,0)+1

max_count = max(count.values())
most_common = [char for char , cnt in count.items() if cnt == max_count]
if len(most_common)>1:
    print("?")
else:
    print(most_common[0].upper())