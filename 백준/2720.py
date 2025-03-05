T = int(input())
coins = [25,10,5,1]
result = []
for i in range(T):
    C = int(input())
    Tc = []
    for coin in coins :
        Tc.append(C//coin)
        C %= coin
    result.append(Tc)
for k in result:
    print(*k)