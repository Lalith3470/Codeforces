a,b=map(int,input().split())
hrs=240-b
cnt=0
for i in range(1,a+1):
    hrs-=i*5
    if hrs>=0:
        cnt+=1
    else:break
print(cnt)
