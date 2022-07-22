
import string
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_numper = input('how many characters for the password?: ')
while True:
    try:
        characters_numper = int(characters_numper)
        if characters_numper < 6:
            print('enter at least 6 characteers')
            characters_numper = input('how many characters for the password?: ')
        else:
            break
    except:
        print('please inter numper')
        characters_numper = input('how many characters for the password?: ')

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_numper * (30/100))
part2 = round(characters_numper * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)
