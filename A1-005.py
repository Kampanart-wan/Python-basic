# month =int(input())
# day =int(input())

# if month <=3 :
#     if month ==3 and day >=21 :
#         season = "spring"
#     else :
#         season = "winter"
# elif month <=6 :
#     if month ==6 and day >=21 :
#         season = "summer"
#     else :
#         season = "spring" 
# elif month <=9 :
#     if month ==9 and day >=21 :
#         season = "fall"
#     else :
#         season = "summer" 
# elif month <=12 :
#     if month ==12 and day >=21 :
#         season = "winter"
#     else :
#         season = "fall"

# print(season)





month = int(input())
day = int(input())

if month >= 3 and day >= 21:
    print("spring")
elif month >= 6 and day >= 21:
    print("summer")
elif month >= 9 and day >= 21:
    print("fall")
elif month >= 12 and day >= 21:
    print("winter")
else:
    print("winter")

