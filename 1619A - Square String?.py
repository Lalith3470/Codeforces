for _ in range(int(input())):
    s=input()
    if len(s)==1:
        print("NO")
    else:
        ln=len(s)//2
        if s[:ln]==s[ln:]:
            print("YES")
        else:
            print("NO")
