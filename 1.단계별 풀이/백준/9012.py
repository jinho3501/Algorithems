T=int(input())

for test_case in range(T):
    stack=[]
    syn=input()
    for i in syn:
        if i=='(':
            stack.append(i)
        elif i==')':
            if len(stack)!=0:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack)!=0:
            print("NO")
        else:
            print("YES")
