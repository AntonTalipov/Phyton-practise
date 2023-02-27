# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# set_1 = set()
# set_2 = set()
# n = int(input('Type a length of set 1: \n'))
# while len(set_1) < n:
#     element = input("Enter element: ")
#     set_1.add(element)
# m = int(input('Type a length of set 2: \n'))
# while len(set_2) < m:
#     element = input("Enter element: ")
#     set_2.add(element)
# print(*set_1)
# print(*set_2)
# set_3 = sorted(set_1.intersection(set_2))
# print(*set_3)
list_1 = []
list_2 = []
n = int(input('Type a length of list 1: \n'))
while len(list_1) < n:
    element = input("Enter element: ")
    list_1.append(element)
m = int(input('Type a length of list 2: \n'))
while len(list_2) < m:
    element = input("Enter element: ")
    list_2.append(element)
print(n, m)
print(*list_1)
print(*list_2)
set_1 = set(list_1)
set_2 = set(list_2)
set_3 = sorted(set_1.intersection(set_2))
print(*set_3)
