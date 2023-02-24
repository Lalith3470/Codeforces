def ans(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if s1>s2:
        return 1
    else:
        return -1
s1=input()
s2=input()
print(ans(s1,s2))
