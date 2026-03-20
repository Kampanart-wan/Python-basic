# water = int(input())
# unit = input().upper()

# if (unit == "C" and water <= 0) or (unit == "F" and water <= 32):
#     print("solid")
# elif (unit == "C" and water >= 100) or (unit == "F" and water >= 212):
#     print("gas")
# else:
#     print("liquid")     
water = int(input())
unit = input().upper()

if unit == "C":
    if water <= 0:
        print("solid")
    elif water >= 100:
        print("gas")
    else:
        print("liquid")
elif unit == "F":
    if water <= 32:
        print("solid")
    elif water >= 212:
        print("gas")
    else:
        print("liquid")