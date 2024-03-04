word = 'jabbwocky'
consonants = 'bcdfghjklmnpqrstvwxyz'
count = 0

for char in word:
    if char.lower() in consonants:
        count += 1

print("Number of consonants:", count)



word = "jabbawocky"
vowels = "aeiou"
count = 0

for char in word:
    if char.lower() not in vowels:
        continue
    count += 1

print("Number of vowels:", count)
