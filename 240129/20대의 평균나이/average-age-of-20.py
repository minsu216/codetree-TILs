i=1
result=0
lst=[]
while True:
    n=int(input())
    if n>=30 and len(lst)==0:
        break
    if n>=30 and len(lst)!=0:
        print("%.2f"%(sum(lst)/(i-1)))
        break
    else:
        lst.append(n)
        i+=1