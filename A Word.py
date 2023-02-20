s=input()
cp_cnt=0
sm_cnt=0
for i in s:
    if i.isupper():
        cp_cnt+=1
    else:
        sm_cnt+=1
if sm_cnt==cp_cnt or sm_cnt>cp_cnt:
    print(s.lower())
else:
    print(s.upper())
