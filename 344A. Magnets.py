n=int(input())
cnt=1
lst=[]
for i in range(n):
    lst.append(input())
val=lst[0]
for i in range(1,n):
    if val!=lst[i]:
        cnt+=1
        val=lst[i]
print(cnt)
