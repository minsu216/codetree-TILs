a,b=map(int,input().split())

flag=False

for j in range(a,b+1):
    if 1920%j==0 and 2880%j==0:
        flag=True
    
if flag:
    print(1)
else:
    print(0)