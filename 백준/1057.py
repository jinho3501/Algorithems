def find(A,B,N):
    round_num= 0
    while N>1 :
        round_num+=1
        if (A-1)// 2 == (B-1)//2:
            return round_num
        A = (A+1)//2
        B = (B+1)//2
        N = (N+1)//2
    return -1


N,A,B =map(int,input().split())
print(find(A,B,N))
