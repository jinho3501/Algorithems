def is_group_word(word):
    seen = set()
    prev_char = ""

    for char in word:
        if char != prev_char:
            if char in seen:
                return  False
            seen.add(prev_char)
        prev_char = char
    return True
T = int(input())
cnt = 0
for _ in range(T):
    word = input()
    if is_group_word(word):
        cnt+=1
print(cnt)