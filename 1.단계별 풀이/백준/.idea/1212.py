num = input().strip()
list = []
for digit in num :
    list.append(format(int(digit),"03b"))
str = ''.join(list)
if str[0] =="0":
    str = str.lstrip("0")
print(str)

# octal_num = input().strip()
# binary_str = ''.join(format(int(digit), '03b') for digit in octal_num)
# if binary_str[0] == '0':
#     binary_str = binary_str.lstrip('0')
# print(binary_str)