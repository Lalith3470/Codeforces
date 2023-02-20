s=input()
vowel="aoyeui"
ans=[]
for i in s:
    if i.lower() not in vowel:
        ans.append(i.lower())
ans=".".join(ans)
print("."+ans)
