money = int(input())
res = 0

res = money % 10
money = money //10
print("10 =",money)

money = res // 5
res = res % 5
print("5 =",money)

money = res // 2
res = res % 2
print("2 =",money)

money = res // 1
res = res % 1
print("1 =",money)