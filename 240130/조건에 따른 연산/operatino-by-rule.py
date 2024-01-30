def a(n):
    global count
    if n>=1000:
        return
    if n%2==0:
        count+=1
        return a((n*3)+1)
    elif n%2!=0:
        count+=1
        return a((n*2)+2)

count=0
n= int(input())

a(n)
print(count)