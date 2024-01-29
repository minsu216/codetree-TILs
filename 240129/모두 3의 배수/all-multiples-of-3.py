count=0
for _ in range(5):
    n=int(input())

    if n%3==0:
        count+=1
if count==5:
    print(1)
else:
    print(0)