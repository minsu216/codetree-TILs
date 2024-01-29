lst=[]
for _ in range(5):
    lst.append(int(input()))
count=0
for i in lst:
    if i %2==0:
        count+=1

print(count)