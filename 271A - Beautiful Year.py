n=int(input())
if n>=1987 and n<2013:
    print(2013)
else:
    i=True
    while i:
        if len(set(str(n+1)))==len(str(n)):
            i=False
        else:
            i=True
        n=n+1
    print(n)
        
