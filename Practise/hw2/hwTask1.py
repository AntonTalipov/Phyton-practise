#  На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Total coins: '))
eagles = 0
tails = 0
for k in range(n):
    i = int(input('Eagle=0, Tails=1: '))
    if i == 0:
        eagles += 1
    if i == 1:
        tails += 1
if eagles > tails:
    print('need turn ', tails, 'tails')
if tails > eagles:
    print('need turn ', eagles, 'eagles')
else:
    print('you can turn ', eagles, 'eagles or', tails, 'tails')

