n=int(input())

for i in range(n):
    print(" "*((n-i)-1)+"*"*((2*i)+1))
for i in range(1,n): # i=1 ->3 , i=2 -> 1
    print(" "*(i) + "*"*(2*(n-i)-1))