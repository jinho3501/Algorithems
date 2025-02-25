A=[]
b=[]
for _ in range(5):
    A.append(list(input().strip()))
for i in range(max(map(len,A))):
       for j in range(5):
           if i < len(A[j]):
            b.append( A[j][i])
print("".join(b))