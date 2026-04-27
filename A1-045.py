s=int(input())
result=(35+((s-1)*5))
result2=(80+((s-10)*8))
if s <= 1 :
    print(35)
elif 1<=s<10 or s==10 :
    print(result)
elif s>10:
    print(result2)