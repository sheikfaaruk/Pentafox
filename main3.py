import random
a=input().lower()
a=a[-1::-1]
a=str(chr(random.randint(65,90)).upper())+a
print(a)
