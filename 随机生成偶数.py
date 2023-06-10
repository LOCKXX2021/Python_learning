import random
a = random.randint(0,99)
b = a%2
while b != 0:
     a = random.randint(0,99)
     b = a%2
print(a)
