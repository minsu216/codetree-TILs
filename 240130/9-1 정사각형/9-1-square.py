n=int(input())
i=9
count=0
real_c=0
while True:
    print(i,end="")
    count+=1
    i-=1
    if count==n:
        print()
        real_c+=1
        count=0
    if i<=0:
        i=9
    if real_c==n:
        break