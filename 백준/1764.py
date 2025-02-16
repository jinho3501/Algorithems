n,m=map(int,input().split())
n_hear=set()
n_see=set()
for i in range(n):
    name=input().strip()
    n_hear.add(name)
for j in range(m):
    name=input().strip()
    n_see.add(name)

result=sorted(list(n_hear & n_see))
print(len(result),*result, sep="\n")
    
    
