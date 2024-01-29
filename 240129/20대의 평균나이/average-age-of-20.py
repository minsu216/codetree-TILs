i=1
result=0
while True:
    n=int(input())
    if n>=30:
        print("%.2f"%(result/(i-1)))
        break
    else:
        result+=n
        i+=1