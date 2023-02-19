# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input('Type max number: \n'))
num = 1
while num <= n:
    print(num, end=" ")
    num *= 2
