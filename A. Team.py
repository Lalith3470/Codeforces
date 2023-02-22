n=int(input())
cnt=0
for i in range(n):
    lst=list(map(int, input().split()))
    if lst.count(1)>1:
        cnt+=1
print(cnt)
