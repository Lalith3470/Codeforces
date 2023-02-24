a=input()
lst=[]
a=a.split()
for i in a:
    val=i[0].upper()+i[1:]
    lst.append(val)
print(" ".join(lst))
