cnt=0
n=int(input())
for i in range(n):
    a=input()
    if a=="++X" or a=="X++":
        cnt+=1
    else:
        cnt-=1
print(cnt)
