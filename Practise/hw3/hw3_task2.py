# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint

a = []
n = int(input('Type a length: \n'))
for i in range(0, n):
    a.append(randint(1, 9))
print(a)
x = int(input('Type a number we need to check: \n'))
number = a[0]
dif_min = x - number
if dif_min < 0:
    dif_min = dif_min * (-1)
for j in range(0, n):
    if a[j] == x:
        number=a[j]
        break
    else:
        dif = x - a[j]
        if dif < 0:
            dif = dif * (-1)
        if dif < dif_min:
            dif_min = dif
            number=a[j]
print(number)
