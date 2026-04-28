num =int(input())
codes =list(map(int,input().split()))

count = {}
for code in codes:
    count[code] = count.get(code, 0) + 1

race_codes = [code for code, count in count.items() if count == 1]
race_codes.sort()

if race_codes:
    print(' '.join(map(str, race_codes)))
else:
    print()