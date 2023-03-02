n=int(input())
lst=list(map(int, input().split()))
if lst.count(1)>=1:
    print("HARD")
else:
    print("EASY")
