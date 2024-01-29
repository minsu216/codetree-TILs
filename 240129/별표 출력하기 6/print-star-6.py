n=int(input())
for i in range(n): # 역방향
    print(' ' * i*2 + '* ' * (((n-i)*2-1)))
# 7,
for i in range(1,n): # 정방향
    print(' ' * (((n-i)-1)*2) + '* ' * (i * 2 + 1))