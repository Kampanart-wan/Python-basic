s = "aeiou"
text = input()
count = 0

for char in text:
    if char in s:
        count += 1

print(count)