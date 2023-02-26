m,n=map(int,input().split())
m=str(m)
for i in range(n):
    if m[-1]=="0":
        m=m[:-1]
    else:
        m=str(int(m)-1)
print(m)
