n = int(input())

F_total = 0
W_total = 0
E_total = 0

for _ in range(n):
    F1, W1, E1, F2, W2, E2 = map(int, input().split())
    
    sum1 = F1 + W1 + E1
    sum2 = F2 + W2 + E2

    if sum1 >= sum2:
        F_total += F1
        W_total += W1
        E_total += E1
    else:
        F_total += F2
        W_total += W2
        E_total += E2

TotalScore = F_total + W_total + E_total

bonus = "YES" if F_total > W_total + E_total else "NO"

print(TotalScore)
print(F_total, W_total, E_total)
print(bonus)