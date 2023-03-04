# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def step(n):
    return n

n = int(input('Type a numbers: \n'))
m = int(input('Type a step: \n'))
sum = 1
while m >= 1:
    sum = sum * step(n)
    m -= 1
print(sum)
