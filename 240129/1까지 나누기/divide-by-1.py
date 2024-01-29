n=int(input())
count=0
re=0
i=1
while True:
    if n==0:
        break
    else:
        re=n//i # 50
        n= re
        count+=1
        i+=1

print(count)