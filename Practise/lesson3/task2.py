from random import randint

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
a = []
n = int(input('Type a length: \n'))
for i in range(0, n):
    a.append(randint(1, 10))
print(a)
k = int(input('Type a number k: \n'))
d = a[k:n] + a[:k]
print(d)
