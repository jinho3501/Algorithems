def gcd(a,b):
    while b:
        a,b =b,a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)

def find_min_lcm(num):
    min_lcm = float('inf')
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                current_lcm = lcm(lcm(num[i],num[j]),num[k])
                min_lcm = min(min_lcm,current_lcm)
    return min_lcm
num = list(map(int,input().split()))
result = find_min_lcm(num)
print(result)

