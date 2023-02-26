# Списки

# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(*list_1) # если поставить * в принте перед названием листа, то значения будут выведены без скобок
# print(list_1)
# print(len(list_1))
# print(list_1[-1])
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_2 = [12, 7, -1, 21, 0]
# print(list_2.pop())  # 0
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# list_2 = [12, 7, -1, 21, 0]
# print(list_2.pop(1))
# list_5 = [3, 5, 1, -5, 3, -10]
# list_5.insert(2,11)
# print(list_5)

# Кортеж - незменяемый список
# t=()
# print(type(t))
# t=(1)
# print(type(t))
# t=(1,)
# print(type(t))

# v = [1, 3, 8]
# print(v)
# v = tuple(v)
# print(v)
#
# a, b, c = v
# print(a, b, c)

# t = (2, 5, 7, 4)
# for i in t:
#     print(i)
# t = (3, 5, 3, 7)
# for i in range(len(t)):
#     print(t[i])

# Словари
# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)
# del dictionary['left']
# print(dictionary)
# for item in dictionary:
#     print('{}:{}'.format(item, dictionary[item]))
# for (k, v) in dictionary.items():
#     print(k, v)

# Множества
# colors = {'red', 'blue', 'green', 'black'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# # colors.remove('red')
# # print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# Операции со множествами в Python
# a = {12, 34, 1, 45, 2, 5}
# b = {4, 23, 5, 12}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i=a.intersection(b)
# print(i)
# dl=a.difference(b)
# print(dl)
# dr=b.difference(a)
# print(dr)
# q=a.union(b).difference(a.intersection(b))
# print(q)
# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)

list_2 = [i for i in range(1, 101)]
print(list_2)
list_3 = [i for i in range(1, 101) if i % 2 == 0]
print(list_3)
list_4 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_4)
list_5 = [i*2 for i in range(1, 101) if i % 2 == 0]
print(list_5)
