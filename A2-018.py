color, num = input().split()

nums = int(num)
color_list=['Red','Green','Blue']

if color =='R':
    order = 0
elif color == 'G' :
    order = 1
elif color == 'B' :
    order = 2

for i in range(nums):
    print(color_list[order], end=" ")
    order = order + 1
    if order > 2 :
        order = 0