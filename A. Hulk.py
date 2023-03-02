n =int(input())
lst=[]
for i in range(1,n):
	if i%2 == 1:
		lst.append("I hate that")
	else:
		lst.append("I love that")
if n%2 == 1:
	lst.append("I hate it")
else:
	lst.append("I love it")
print(" ".join(lst))
