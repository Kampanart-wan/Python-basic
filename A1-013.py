text =input()
num =int(input())
if text==('H') and num==4567 :
    print("safe unlocked")
elif text==('H') and num!=4567 :
    print("safe locked - change digit")
elif text!=('H') and num==4567 :
    print("safe locked - change char")    
else :
    print("safe locked")