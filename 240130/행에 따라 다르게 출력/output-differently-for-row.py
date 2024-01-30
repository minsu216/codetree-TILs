n=int(input())
count=0
for i in range(1,n+1):
    for j in range(n):
        if i%2!=0:
            count+=1
            print(count,end=" ")
        if i%2 ==0:
            count+=2
            print(count,end=" ")
    print()