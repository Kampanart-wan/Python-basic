# age, day = input().split()
# age2=int(age)
# price=0
# price2=100
# price3=150
# result=(price/2)
# result2=(price2/2)
# result3=(price3/2)
# Day_list=("Mon","Tue","Thu","Fri","Sat","Sun")


# if age2 < 5 and day in Day_list:
#     print(0)
# elif 5<=age2<=18 and day in Day_list:
#     print(100)
# elif age2>=19 and day in Day_list:
#     print(150)
  
# elif day=="Wed" and age2<5 :
#     print(result)
# elif day=="Wed" and 5<=age2<=18 :
#     print(result2)
# elif day=="Wed" and age2>=19 :
#     print(result3)
age, day = input().split()
age = int(age)

if day == "Wed":
    if age < 5:
        print(0)
    elif 5 <= age <= 18:
        print(50)
    else:
        print(75)
else:
    if age < 5:
        print(0)
    elif 5 <= age <= 18:
        print(100)
    else:
        print(150)