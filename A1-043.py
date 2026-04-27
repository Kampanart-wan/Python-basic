score = int(input())
bonus = int(input())
day = int(input())
key = [0, 1, 2, 3, 4, 5]

if day <= 3:
    sumscore = score + bonus
elif day > 3:
    sumscore = ( score + bonus ) * 1.5

print(int(sumscore))

if sumscore >= 1500:
    print(key[5])
elif sumscore >= 1000 and sumscore < 1500 :
    print(key[4])
elif sumscore >= 500 and sumscore < 1000 :
    print(key[3])
elif sumscore >= 200 and sumscore < 500:
    print(key[2])
elif sumscore < 200:
    print(key[1])

if sumscore >= 1500 and day >= 7 :
    print(99)
elif sumscore >= 1000 and sumscore < 1500 :
    print(88)
else:
    print(0)