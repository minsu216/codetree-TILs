n=int(input())
count=0
re=0
i=1
while True:
    re=n//i # 50
    n= re
    count+=1
    i+=1
    if re==0:
        break
print(count)