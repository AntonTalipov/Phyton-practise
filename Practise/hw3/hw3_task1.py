# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint

a = []
n = int(input('Type a length: \n'))
for i in range(0, n):
    a.append(randint(1, 5))
print(a)
count = 0
x = int(input('Type a number we need to check: \n'))
for j in range(0, n):
    if a[j] == x:
        count += 1
print(count)
