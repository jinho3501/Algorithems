from collections import deque

T=int(input())
for test_case in range(T):
    method=input().strip()
    num=int(input())
    arr=input()[1:-1].split(',')


    queue=deque(arr)
    flag = 0 
    
    if num==0:
        queue=[]
    
    for i in method:
        if i == 'R':
            flag+=1
        elif i == 'D':
            if len(queue)==0:
                print("error")
                break
            else:
                if flag%2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")