i = 1
result = 0
lst = []

while True:
    try:
        n = int(input())
        if n < 20 or n >= 30: # 20이하 30이상이면 종료
            break
        else:
            lst.append(n)
            i += 1
    except EOFError:
        break

if lst:  # lst가 비어있지 않은 경우만 평균 계산
    print("%.2f" % (sum(lst) / (i - 1)))