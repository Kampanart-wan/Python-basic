w, l, n = map(int, input().split())
pricepermeter  = int(input())
permeter = 2 * (w + l)
totalwire = permeter * n
totalprice = totalwire * pricepermeter
print(totalwire)
print(totalprice)