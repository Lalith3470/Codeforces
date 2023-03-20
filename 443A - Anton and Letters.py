n=input()
n=n[1:-1]
if not n:print(0)
else:
    n=n.split(",")
    n=[i.strip() for i in n]
    print(len(set(n)))
