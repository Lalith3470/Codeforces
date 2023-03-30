for _ in range(int(input())):
    a,b=map(int,input().split())
    v=a%b
    if a%b==0:print(0)
    else:
        print(b-v)
    
