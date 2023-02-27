# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

string = list(input('Type a sting: \n'))
d = {}.fromkeys(string, 0)
print(d)
for i in string:
    print(f"{i}_{d[i]}" if d[i] else i, end=" ")
    d[i] += 1