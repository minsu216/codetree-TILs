n= int(input())

for i in range(n,0,-1):
    for j in range(i):  #4 3 
        print("*",end="")
    print(" "*(n-i),end="")
    print(" "*(n-i),end="")
    for k in range(i): 
        print("*",end="")

    print()