K,Q,L,B,N,P = map(int,input().split())
need = {"K":1,"Q":1,"L":2,"B":2,"N":2,"P":8}
current = {"K":K,"Q":Q,"L":L,"B":B,"N":N,"P":P}
for piece in need:
    diff = need[piece] - current[piece]
    print(diff)