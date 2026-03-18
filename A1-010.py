age =int(input())
Relate = input()

# if age < 18 or Relate =="s" or Relate == 'S':
if age < 18 or Relate in ['s','S'] :
    print(20)

else:
    print(50)