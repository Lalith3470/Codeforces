
stack=[]
n=int(input())
s=input()
for i in range(n):
    if stack and stack[-1]==s[i]:
        continue
    else:
        stack.append(s[i])
print(n-len(stack))
