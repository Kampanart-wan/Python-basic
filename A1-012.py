number = input()
sign =input()
reverse= number[::-1]
result =(int(number)+int(reverse))
result2 =(int(number)*int(reverse))
 
if sign =="+" :
  txt =f"{number} {sign} {int(reverse)} = {result}  "
  print(txt)
elif sign =="*" : 
  txt =f"{number} {sign} {int(reverse)} = {result2}  "
  print(txt)