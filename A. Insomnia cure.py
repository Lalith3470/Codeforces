k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
lst=[k,l,m,n]
c=0
if 1 in lst:print(d)
else:
    for i in range(d+1):
        if i%lst[0]!=0 and i%lst[1]!=0 and i%lst[2]!=0 and i%lst[3]!=0:
            c+=1
    print(d-c)
