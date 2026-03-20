period = int(input())
time = int(input())

if time == 0 or period==0:
    print("No teaching")
else:
    total = period * time
    hours = total // 60
    minutes = total % 60

    if minutes == 0:
        print(f"{hours} hours")
    elif hours == 0:
        print(f"{minutes} minutes")
    else:
        print(f"{hours} hours {minutes} minutes")

