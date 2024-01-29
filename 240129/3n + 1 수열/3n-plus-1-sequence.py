n=int(input())
count=0
def aa(n):
    global count
    if n==1:
        return
    if n%2==0:
        count+=1
        return aa(n//2)
    else:
        count+=1
        return aa((n*3)+1)

aa(n)
print(count)