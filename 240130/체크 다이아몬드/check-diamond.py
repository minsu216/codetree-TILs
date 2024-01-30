n=int(input())

for i in range(n):
    print(" "*((n-i)-1)+"* "*(i+1))
for i in range(1,n): # i= 1,2
    print(" "*i+ "* "*((n-i)))#3-1