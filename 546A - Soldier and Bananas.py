k,n,w=map(int, input().split())
i=1
cost=0
while i<=w:
    cost+=i*k
    i+=1
if cost>n:
    print(cost-n)
else:
    print(0)
