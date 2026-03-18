num=int(input())
num2=int(input())
num3=int(input())

if num==num2==num3:
    print("all the same")
elif num!=num2 and num2!=num3 and num3!=num :
    print("all different")
else:
    print("neither")