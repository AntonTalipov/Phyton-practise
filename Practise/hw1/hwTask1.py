# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
b = 0
a = int(input("type a number: \n"))
if a / 100 >= 1 and a / 100 < 10:
    while a >= 1:
        b = b + a % 10
        a = a // 10
    print(b)
else:
    print(" incorrect number")
