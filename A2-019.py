# text= input()
# word = ['B', 'U', 'U']
# reult = ''
# count = 0
# numU=0

# for i in range(len(text)-2) :
#     if text[i] == 'b' or text[i] == 'B':
#         if text[i+1]=='u' or text[i+1]=='U':
#             if text[i+2]=='u' or text[i+2]=='U':
#                 numU=2
#                 for j in range(i+3,len(text)) :
#                     if text[j] == 'u' or text[j] == 'U':
#                         numU+= 1
# if numU==0:
#     if 'b' in text or 'B' in text:
#         for i in range(len(text)):
#             if text[i]=='b' or text[i]=='B':
#                 text2=text[0:i+1]
#                 for j in range(i+1,len(text)) :
#                     text2+='U'
#     else:
#         text2=''
#         for i in range(len(text)):
#             if i%3==0:
#                 text2+='B'
#             else:
#                 text2+='U'
#     print(text2)
# else:            
#     print(f'Yes {numU}')
text = input()
text_up = text.upper()
max_U = 0

for i in range(len(text)) :
    if text[i] == 'B' :
        current_U = 0
        new_U = 0
        
        for j in range( i + 1, len(text_up)) :
            if text_up[j] == 'U':
                current_U += 1
            elif text_up[j] == 'B':
                
                for k in range( j + 1, len(text_up)) :
                    if text_up[k] == 'U':
                        new_U += 1
                        current_U = 0
                    else:
                        break
            else:
                break
        
        max_U = max(max_U, current_U, new_U)
        
if max_U >= 2:
    print(f'Yes {max_U}')
elif 'B' in text_up :
    where_B = text_up.find('B')
    result = text[:where_B + 1] + ( 'U' * (len(text) - where_B - 1))
    
    print(result)
else:
    word = 'BUU' * 3
    print(word[:len(text)])
        