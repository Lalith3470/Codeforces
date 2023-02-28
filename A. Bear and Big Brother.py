a,b=map(int, input().split())
cnt=0
i=True
while i:
    cnt+=1
    a=a*3
    b=b*2
    if a>b:
        i=False
print(cnt)
    
