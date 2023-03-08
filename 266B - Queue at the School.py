t,sec=map(int, input().split())
n=input()
n=[i for i in n]
while sec>0:
    S=""
    k=0
    while k<t-1:
        if n[k]=="B" and n[k+1]=="G":
            n[k]="G"
            n[k+1]="B"
            k+=1
        k+=1
    sec-=1
print("".join(n))
        
        
