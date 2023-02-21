for _ in range(int(input())):
    s=input()
    if len(s)<=10:
        print(s)
    else:
        ln=len(s)
        print(s[0]+str(ln-2)+s[ln-1])
