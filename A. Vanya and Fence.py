a,b=map(int, input().split())
l=list(map(int, input().split()))
cnt=0
for i in l:
    if i<=b:
        cnt+=1
    else:
        cnt+=2
print(cnt)
