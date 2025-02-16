M,N = map(int,input().split())
board = [input().strip() for _ in range(M)]
min_change = float('inf')
for i in range(M-7):
    for j in range(N-7):
        count1 = 0
        count2 = 0
        for x in range(8):
            for y in range(8):
                if (x+y)%2==0 :
                    color1="W"
                else:
                    color1="B"
                if board[i+x][j+y] != color1:
                    count1+=1
                if (x+y)%2==0 :
                    color2="B"
                else:
                    color2="W"
                if board[i+x][j+y] != color2:
                    count2+=1
        min_change = min(min_change,count1,count2)
print(min_change)

