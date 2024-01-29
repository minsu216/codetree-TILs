# result=0
# for i in range(1,7):
#     n=int(input())
#     if n>=30:
#         print("%.2f"%(result/(i-1)))
#     else:
#         result+=n

i=0
result=0
while True:
    n=int(input())
    if n>=30:
        print("%.2f"%(result/i))
        break
    else:
        result+=n
        i+=1