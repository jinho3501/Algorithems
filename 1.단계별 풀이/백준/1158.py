a,b = map(int,input().split())
queue=[i for i in range(1,a+1)]
result=[]
num=0
for j in range(a):
    num+=b-1
    if num>=len(queue):
        num%=len(queue)
    result.append(str(queue[num]))
    queue.pop(num)
print("<",','.join(result),">",sep="")
