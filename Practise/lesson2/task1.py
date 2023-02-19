# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

def Factorial(n):
    if n == 0:
        return 0
    if n >= 1:
        sum = 1
        i = 1
        while i < n:
            sum = sum * (i + 1)
            i += 1
    return sum


print(Factorial(5))