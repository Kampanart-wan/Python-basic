size, type = input().split()
topping=input().split()

price_list={('S','R'):60,('S','T'):80,('M','R'):80,('M','T'):100,('L','R'):100,('L','T'):120,}
price= price_list[(size, type)]

if topping[0]=='P':
    amount=int(topping[1])
    price += 15 * amount
elif topping[0]=='E':
    amount=int(topping[1])
    price+=10*amount

print(price)    

