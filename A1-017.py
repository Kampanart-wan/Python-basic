year=input()
month=input()
day=input()
year2=input()
month2=input()
day2=input()

if year > year2 :
    print(2)
elif year2 > year :
    print(1)
elif year == year2 and month>month2 :
    print(2)
elif year == year2 and month<month2 :
    print(1)
elif year == year2 and month == month2 and day>day2 :
    print(2)
elif year == year2 and month == month2 and day<day2 :
    print(1)
else :
    print(0)