import math

def is_prime(radius):
    if radius < 2:
        return False
    
    for i in range(2, int(math.sqrt(radius)) + 1):
        if radius % i == 0:
            return False
    return True

n = int(input())

if is_prime(n):
    print("Yes")

    special_numbers = []
    for i in range(2, n + 1):
        if is_prime(i) :
            special_numbers.append(i)
    
    print(*special_numbers)
else:
    print("No")