n = int(input())
codes = list(map(int, input().split()))

counts = {}
for code in codes:
    counts[code] = counts.get(code, 0) + 1

rare_codes = [code for code, count in counts.items() if count == 1]
rare_codes.sort()

if rare_codes:
    print(' '.join(str(code) for code in rare_codes))
else:
    print()