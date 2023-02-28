t= int(input())
val=0
ans=0
for i in range(t):
    a,b=map(int, input().split())
    ans+=-a+b
    val=max(val,ans)
print(val)
