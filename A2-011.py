nums = list(map(int, input().split()))
set_num = set()
ans = []
for num in nums:
    if num not in set_num:
        set_num.add(num)
        ans.append(num)

print(*ans)