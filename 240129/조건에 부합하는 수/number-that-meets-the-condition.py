a= int(input())
# 짝수이면서 
for i in range(1,a+1):
    if i%2==0 and i%4!=0:
        continue
    elif (i//8)%2==0:
        continue
    elif (i%7)<4:
        continue
    else:
        print(i,end=' ')