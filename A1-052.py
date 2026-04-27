money=int(input())
res = 0

if 100<=money<=20000 and money%100==0:
    res = money // 1000
    if res>0:
        print("1000 =",res)
    money=money%1000
 
    res = money // 500
    if res>0:
        print("500 =",res)
    money=money%500

    res = money // 100
    if res>0:
        print("100 =",res)
    money=money%100

else:
    print("ERROR")

       
        