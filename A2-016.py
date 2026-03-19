
lotto = input()
win = input()

if lotto == win:
    print(1000000)
elif lotto[2:7] == win[2:7]:
    print(100000)
elif lotto[4:7] == win[4:7] and lotto[0] == win[0] :
    print(2000)
elif lotto[5:7] == win[5:7] and lotto[0] == win[0] :
    print(1000)
elif lotto[4:7] == win[4:7] and lotto[0] != win[0] :
    print(200)  
elif lotto[5:7] == win[5:7] and lotto[0] != win[0] :
    print(100)
elif lotto[2:7] != win[2:7] and lotto[0] == win[0] :
    print(20)
else:
    print(0)



