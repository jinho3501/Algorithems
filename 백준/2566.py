A=[]
max_value = 0
row,col=0,0
for _ in range(9):
    A.append(list(map(int,input().split())))
for i in range(9):
   for j in range(9):
       if A[i][j] > max_value:
           max_value = A[i][j]
           row,col = i,j
print(max_value)
print(row+1, col+1)
